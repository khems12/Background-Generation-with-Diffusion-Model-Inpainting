import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np 
import rembg

from main import bg_generator

st.set_page_config(layout="wide")

# Streamlit app title
st.title("Image Upload and Prompt-Based Image Generation")

# Create two columns
col1, col2 = st.columns(2)

# First column for uploading and prompt
with col1:
    # Upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image in the first column
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)


# Second column for displaying the generated image
with col2:

    # Input field for prompt
    prompt = st.text_input("Enter a prompt for image generation:")

    # Button to trigger image generation
    if st.button("Generate Image"):
        # Placeholder for image generation logic
        st.write(f"Generating image based on the prompt: '{prompt}'")
        # Simulate image generation here or replace with your generation code

        if uploaded_file is not None and 'prompt' in locals():
            bg_image = bg_generator(image, prompt)
            st.image(bg_image, caption="Generated Image", use_column_width=True)
