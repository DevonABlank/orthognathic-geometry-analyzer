"""
jawproject.landmarks

Face landmark detection utilities using MediaPipe Tasks (FaceLandmarker).

What it does:
- Loads/ensures a FaceLandmarker model file exists locally
- Runs MediaPipe's FaceLandmarker on an RGB image
- Returns normalized (x, y) face mesh landmarks for the first detected face

Notes:
- On first run, the model may be downloaded into /assets (requires internet once).
- After the model file exists locally, detection can run offline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import numpy as np
import mediapipe as mp


@dataclass(frozen=True)
class Landmark:
    x: float
    y: float


def detect_face_mesh_landmarks(rgb_image: np.ndarray) -> Optional[List[Landmark]]:
    """
    Uses MediaPipe Tasks FaceLandmarker (new API).
    Returns normalized landmarks for first detected face.
    """

    # Lazy import to avoid global init issues
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision

    h, w, _ = rgb_image.shape

    base_options = python.BaseOptions(model_asset_path=_get_model_path())
    options = vision.FaceLandmarkerOptions(
        base_options=base_options,
        output_face_blendshapes=False,
        output_facial_transformation_matrixes=False,
        num_faces=1,
    )

    detector = vision.FaceLandmarker.create_from_options(options)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
    result = detector.detect(mp_image)

    if not result.face_landmarks:
        return None

    face_landmarks = result.face_landmarks[0]

    return [Landmark(lm.x, lm.y) for lm in face_landmarks]


def _get_model_path() -> str:
    """
    Downloads the face landmark model if missing.
    """
    import os
    import urllib.request

    model_dir = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, "face_landmarker.task")

    if not os.path.exists(model_path):
        url = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
        print("Downloading MediaPipe face landmark model...")
        urllib.request.urlretrieve(url, model_path)

    return model_path