Quick start:

streamlit run src/jawproject/app.py


# Jaw Profile Prototype (MVP)

A small computer-vision demo that detects face landmarks and computes a simple
chin-to-vertical-line metric on uploaded profile images.

> Prototype only. Not a medical diagnostic tool.


## Features

- Upload profile images (JPG/PNG)
- Detect 3D face mesh landmarks using MediaPipe FaceLandmarker
- Compute a chin-to-vertical-line distance metric (MVP heuristic)
- Visualize landmarks, reference line, and measurement overlay
- Local web interface using Streamlit

---

## Tech Stack

- Python 3.10+
- Streamlit (web UI)
- MediaPipe Tasks API (face landmark detection)
- OpenCV (image processing)
- NumPy (numerical operations)

---

## Project Structure
```
JawProject/
├── README.md
├── pyproject.toml
├── .gitignore
├── assets/                 # MediaPipe face landmark model
├── src/
│   └── jawproject/
│       ├── app.py          # Streamlit web app entrypoint
│       ├── landmarks.py   # Face landmark detection (MediaPipe Tasks API)
│       ├── measure.py     # Jaw metric computation logic
│       ├── visualize.py   # Visualization and overlay drawing
│       └── __init__.py
├── tests/
│   └── test_smoke.py
└── .github/
```

## How It Works

1. The user uploads a face image via the browser.
2. The image is decoded and converted to RGB.
3. MediaPipe FaceLandmarker detects facial landmarks.
4. Two landmarks are selected:
   - Subnasale (near base of nose)
   - Chin (menton region)
5. A vertical reference line is defined through the subnasale point.
6. The horizontal distance from the chin to this line is computed in pixels.
7. Results are visualized on the image and displayed numerically.

---

## Running the App

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```
### 2. Install Dependencies
```pip install -e .```

### 3. Run the Streamlit app
```streamlit run src/jawproject/app.py```
