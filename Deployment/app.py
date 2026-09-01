import time
import streamlit as st
import numpy as np
from PIL import Image
import urllib.request
from utils import *

# Load class labels
labels = gen_labels()

# HTML header and images
html_temp = '''
  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: -50px">
    <div style = "display: flex; flex-direction: row; align-items: center; justify-content: center;">
     <center><h1 style="color: #000; font-size: 50px;"><span style="color: #0e7d73">Smart </span>Garbage</h1></center>
    <img src="https://cdn-icons-png.flaticon.com/128/1345/1345823.png" style="width: 0px;">
    </div>
    <div style="margin-top: -20px">
    <img src="https://i.postimg.cc/W3Lx45QB/Waste-management-pana.png" style="width: 400px;">
    </div>   
    </div>
    '''
st.markdown(html_temp, unsafe_allow_html=True)

html_temp = '''
    <div>
    <center><h3 style="color: #008080; margin-top: -20px">Check the type here </h3></center>
    </div>
    '''
st.markdown(html_temp, unsafe_allow_html=True)

# Upload or link options
opt = st.selectbox("How do you want to upload the image for classification?\n", 
                   ('Please Select', 'Upload image via link', 'Upload image from device'))

image = None

if opt == 'Upload image from device':
    file = st.file_uploader('Select', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        image = Image.open(file).convert('RGB')  # Ensure 3-channel RGB image

elif opt == 'Upload image via link':
    img_url = st.text_input('Enter the Image URL')
    if img_url:
        try:
            image = Image.open(urllib.request.urlopen(img_url)).convert('RGB')
        except Exception:
            st.error("Please enter a valid image URL!")

if image is not None:
    st.image(image, width=300, caption='Uploaded Image')
    if st.button('Predict'):
        try:
            # Preprocess function should resize and scale the image as expected by model
            img = preprocess(image)  # Assumes preprocess returns a numpy array scaled correctly
            
            # Load model architecture and weights
            model = model_arc()  # Your model architecture function from utils.py
            model.load_weights("../weights/modelnew.h5")  # Adjust path if needed
            
            prediction = model.predict(img[np.newaxis, ...])
            
            predicted_label = labels[np.argmax(prediction[0], axis=-1)]
            st.info(f'Hey! The uploaded image has been classified as "{predicted_label}" product')
        
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")
