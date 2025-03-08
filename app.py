import cv2
import numpy as np
import streamlit as st
from io import BytesIO

def convert_to_sketch(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_img = cv2.bitwise_not(gray_img)
    blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blur_img = cv2.bitwise_not(blurred_img)
    sketch_img = cv2.divide(gray_img, inverted_blur_img, scale=256.0)
    return sketch_img

# Streamlit UI
st.title("Pencil Sketch Converter")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert file to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Convert to sketch
    sketch_img = convert_to_sketch(img)
    
    # Display original and sketch images
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, channels="BGR", caption="Original Image")
    with col2:
        st.image(sketch_img, caption="Sketch Image", use_container_width=True)
    
    # Convert sketch image to bytes for download
    _, buffer = cv2.imencode(".png", sketch_img)
    byte_im = buffer.tobytes()
    
    st.download_button(label="Download Sketch", data=byte_im, file_name="sketch.png", mime="image/png")
