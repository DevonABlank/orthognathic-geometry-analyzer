Quick start:

streamlit run src/jawproject/app.py

# Orthognathic Geometry Analyzer

A computer vision web application for detecting facial landmarks and computing geometric jaw profile measurements from uploaded images.

> **Medical Disclaimer**: This is a research/educational prototype and not a medical diagnostic tool. Not intended for clinical use.

## Features

- **Facial Landmark Detection**: Utilizes MediaPipe's 3D face mesh model for precise landmark identification
- **Geometric Measurement**: Computes chin-to-vertical reference line distances using anatomical landmarks
- **Interactive Visualization**: Real-time overlay of detected landmarks, reference lines, and measurements
- **Web-Based Interface**: User-friendly Streamlit application for image upload and analysis
- **Modular Architecture**: Clean separation of detection, measurement, and visualization logic

## Technical Highlights

- **Computer Vision Pipeline**: Implements end-to-end CV workflow from image processing to geometric analysis
- **MediaPipe Integration**: Leverages Google's MediaPipe Tasks API for robust 3D facial landmark detection
- **Anatomical Landmarks**: Uses clinically-relevant reference points (subnasale, menton) for measurements
- **Reproducible Environment**: Virtual environment management with dependency specification
- **Modular Design**: Separated concerns across detection, computation, and visualization modules
- **Test Coverage**: Includes automated testing framework with pytest

## Technologies

- Python 3.10+
- Streamlit (web framework)
- MediaPipe Tasks API (facial landmark detection)
- OpenCV (image processing)
- NumPy (numerical computations)
- Pytest (testing framework)

## Project Structure
```
orthognathic-geometry-analyzer/
├── README.md
├── pyproject.toml
├── .gitignore
├── assets/                 # MediaPipe face landmark model
├── src/
│   └── jawproject/
│       ├── app.py          # Streamlit web app entrypoint
│       ├── landmarks.py    # Face landmark detection module
│       ├── measure.py      # Geometric measurement logic
│       ├── visualize.py    # Visualization and overlay rendering
│       └── __init__.py
├── tests/
│   └── test_smoke.py       # Automated test suite
└── .github/
```

## How It Works

1. **Image Upload**: User uploads a profile face image (JPG/PNG) through the web interface
2. **Preprocessing**: Image is decoded and converted to RGB format using OpenCV
3. **Landmark Detection**: MediaPipe FaceLandmarker identifies 3D facial landmarks
4. **Reference Point Selection**: Algorithm selects anatomical landmarks:
   - **Subnasale**: Base of the nose (vertical reference)
   - **Menton**: Chin prominence point
5. **Geometric Calculation**: Computes horizontal distance from chin to vertical reference line through subnasale
6. **Visualization**: Overlays landmarks, reference line, and measurement on original image
7. **Results Display**: Shows annotated image with numerical measurement in pixels

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/DevonABlank/orthognathic-geometry-analyzer.git
cd orthognathic-geometry-analyzer
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -e .
```

### 4. Run the Application
```bash
streamlit run src/jawproject/app.py
```

The application will open in your default browser at `http://localhost:8501`

## Testing

Run the test suite:
```bash
pytest tests/
```

## Measurement Methodology

The application implements a simplified geometric analysis:
- **Vertical Reference**: Defined by a vertical line passing through the subnasale landmark
- **Horizontal Distance**: Measured perpendicular from the menton (chin) to the reference line
- **Units**: Measurements are in pixels (not calibrated to physical units)

**Note**: This is a heuristic measurement for educational/research purposes, not a validated clinical assessment tool.

## Future Enhancements

- Physical unit calibration using reference markers
- Multiple measurement metrics (facial convexity angle, pogonion analysis)
- Batch processing capabilities
- Export functionality for measurements and annotated images
- Comparison with normative data

## Academic Context

Personal project exploring computer vision applications in biomedical geometry analysis, demonstrating integration of modern CV libraries (MediaPipe, OpenCV) with interactive web frameworks (Streamlit) for practical measurement applications.

## License

MIT License
