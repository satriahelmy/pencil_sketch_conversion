# Pencil Sketch Converter

This is a simple web application that converts an uploaded image into a pencil sketch using OpenCV and Streamlit.

## Features
- Upload an image (JPG, JPEG, PNG)
- Convert the image to a pencil sketch
- Preview both the original and sketch images side by side
- Download the generated sketch as a PNG file

## Installation
Ensure you have Python installed, then install the required dependencies:

```bash
pip install streamlit opencv-python numpy
```

## Usage
Run the application using Streamlit:

```bash
streamlit run app.py
```

Replace `app.py` with the actual filename if different.

## How It Works
1. The uploaded image is read using OpenCV.
2. It is converted to grayscale.
3. An inverted version of the grayscale image is created.
4. A Gaussian blur is applied to the inverted image.
5. The blurred image is inverted again.
6. The grayscale image is divided by the inverted blurred image to create the sketch effect.

## Dependencies
- `streamlit` (for web interface)
- `opencv-python` (for image processing)
- `numpy` (for array manipulations)
