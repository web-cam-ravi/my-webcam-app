import streamlit as st
import cv2
import numpy as np

st.title("AIML BATCH - Photo Frame App")

picture = st.camera_input("Take a photo")

if picture:
    bytes_data = picture.getvalue()
    cv_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    height, width, _ = cv_img.shape
    cv2.rectangle(cv_img, (10, 10), (width - 10, height - 10), (0, 255, 0), 5)

    rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    st.image(rgb_img, caption="Framed Snapshot")
