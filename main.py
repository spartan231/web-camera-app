import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # Start camera
    camera_image = st.camera_input("Camera")

if camera_image is not None:
    #Create a pillow image instance
    img = Image.open(camera_image)

    # Convert pillow image to grayscale
    #gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(img)
