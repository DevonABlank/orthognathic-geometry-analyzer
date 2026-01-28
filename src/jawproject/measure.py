"""
jawproject.measure

Measurement and scoring logic for the Jaw Profile Prototype.

What it does:
- Selects two landmark points (subnasale + chin) using MediaPipe landmark indices
- Defines a vertical reference line through subnasale (TVL-ish)
- Computes signed horizontal pixel distance from the line to the chin point

Notes:
- MVP heuristic; sign can flip depending on whether the face is left- or right-facing.
- Future work: orientation normalization + more robust cephalometric-style metrics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

from jawproject.landmarks import Landmark


# NOTE: MediaPipe Face Mesh landmark indices.
# These are reasonable *approximations* for an MVP.
# We'll refine later after visual verification.
SUBNASALE_IDX = 2        # near nose base / subnasale region
CHIN_IDX = 152           # chin (menton-ish) - commonly used


@dataclass(frozen=True)
class JawMetric:
    subnasale_xy: Tuple[float, float]  # normalized coords
    chin_xy: Tuple[float, float]       # normalized coords
    chin_to_tvl_px: float              # signed pixels (positive = chin ahead of line)
    is_behind_line: bool


def compute_chin_to_vertical_line(landmarks: List[Landmark], image_w: int) -> JawMetric:
    """
    Define a vertical reference line (TVL-ish) at subnasale x-position.
    Compute signed horizontal pixel distance from that line to chin x-position.
    """
    sub = landmarks[SUBNASALE_IDX]
    chin = landmarks[CHIN_IDX]

    sub_x_px = sub.x * image_w
    chin_x_px = chin.x * image_w

    # Signed distance: chin minus subnasale
    # + => chin is more to the right than line, - => left than line
    # For left-facing vs right-facing profiles, the sign will flip.
    dist_px = chin_x_px - sub_x_px

    return JawMetric(
        subnasale_xy=(sub.x, sub.y),
        chin_xy=(chin.x, chin.y),
        chin_to_tvl_px=float(dist_px),
        is_behind_line=(dist_px < 0),
    )