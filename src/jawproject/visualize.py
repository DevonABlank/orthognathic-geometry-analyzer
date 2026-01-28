"""
jawproject.visualize

Visualization utilities for drawing landmarks and metric overlays on images.

What it does:
- Draws all landmarks (optional)
- Draws the measurement overlay:
  - vertical reference line through subnasale
  - dot at subnasale and chin
  - text label showing the computed metric
"""

from __future__ import annotations

from typing import List, Optional, Tuple

import numpy as np
import cv2

from jawproject.landmarks import Landmark
from jawproject.measure import JawMetric


def _to_px(lm: Landmark, w: int, h: int) -> Tuple[int, int]:
    return int(lm.x * w), int(lm.y * h)


def draw_landmarks(rgb_image: np.ndarray, landmarks: List[Landmark]) -> np.ndarray:
    out = rgb_image.copy()
    h, w = out.shape[:2]

    for lm in landmarks:
        cx, cy = _to_px(lm, w, h)
        cv2.circle(out, (cx, cy), 1, (0, 255, 0), -1)

    return out


def draw_metric_overlay(
    rgb_image: np.ndarray,
    landmarks: List[Landmark],
    metric: JawMetric,
) -> np.ndarray:
    """
    Draw:
      - vertical line through subnasale (TVL-ish)
      - dot at subnasale and chin
      - text with signed distance
    """
    out = rgb_image.copy()
    h, w = out.shape[:2]

    sub = Landmark(*metric.subnasale_xy)
    chin = Landmark(*metric.chin_xy)

    sub_px = _to_px(sub, w, h)
    chin_px = _to_px(chin, w, h)

    # Vertical line through subnasale
    cv2.line(out, (sub_px[0], 0), (sub_px[0], h), (255, 255, 0), 2)

    # Key points
    cv2.circle(out, sub_px, 5, (255, 255, 0), -1)
    cv2.circle(out, chin_px, 6, (255, 0, 255), -1)

    # Distance text
    txt = f"chin_to_TVL_px: {metric.chin_to_tvl_px:.1f} ({'behind' if metric.is_behind_line else 'ahead'})"
    cv2.putText(out, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    return out