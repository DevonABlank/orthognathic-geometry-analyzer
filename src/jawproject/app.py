"""
jawproject.app

Streamlit web app entrypoint for the Jaw Profile Prototype.

What it does:
- Lets a user upload a face image (jpg/png)
- Runs face landmark detection (MediaPipe Face Landmarker)
- Computes a simple chin-to-vertical-line metric (MVP heuristic)
- Visualizes the result by drawing a reference line + key points + score overlay

Notes:
- This is an engineering demo / prototype for geometry-based facial measurement.
- Not a medical diagnostic tool.
"""

import streamlit as st
import numpy as np
import cv2

from jawproject.measure import compute_chin_to_vertical_line
from jawproject.visualize import draw_landmarks, draw_metric_overlay
from jawproject.landmarks import detect_face_mesh_landmarks
from jawproject.visualize import draw_landmarks


st.set_page_config(page_title="Jaw Profile Prototype", layout="centered")

st.title("Jaw Profile Prototype (MVP)")
st.write(
    "Upload a face image. This MVP detects face mesh landmarks and draws them. "
    "Next step: compute a simple chin-vs-reference-line metric."
)

uploaded = st.file_uploader("Upload an image (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    file_bytes = np.frombuffer(uploaded.read(), np.uint8)
    bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if bgr is None:
        st.error("Could not read that image. Try a different file.")
        st.stop()

    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    landmarks = detect_face_mesh_landmarks(rgb)

    if landmarks is None:
        st.warning("No face detected. Try a clearer photo.")
        st.image(rgb, caption="Input", use_container_width=True)
        st.stop()

    metric = compute_chin_to_vertical_line(landmarks, image_w=rgb.shape[1])
    annotated = draw_metric_overlay(rgb, landmarks, metric)

    st.metric("Chin-to-TVL (px)", f"{metric.chin_to_tvl_px:.1f}")
    st.caption("Note: MVP heuristic. Sign depends on whether face is left- vs right-facing.")

    st.image(rgb, caption="Input", use_container_width=True)
    st.image(annotated, caption="Landmarks (MVP)", use_container_width=True)
    st.success("Landmarks detected successfully.")