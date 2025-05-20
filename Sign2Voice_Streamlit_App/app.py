
import streamlit as st
from gtts import gTTS
from PIL import Image
import time
import os

st.set_page_config(page_title="Sign2Voice", layout="centered")
st.title("🧠 Sign2Voice – Bangla Sign Language to Voice Translator")
st.markdown("### Empowering Silence with Sound")

# Navigation
page = st.sidebar.radio("Go to", ["Home", "Real-time Detection", "Text to Speech", "Learn Signs", "Emergency SOS"])

if page == "Home":
    st.image("images/logo.png", width=200)
    st.write("Welcome to **Sign2Voice**, a real-time translator of Bangla Sign Language into natural Bangla voice using AI.")
    st.markdown("### Key Features:")
    st.markdown("- Real-time Bangla Sign Detection")
    st.markdown("- Bangla Text to Speech")
    st.markdown("- Gesture Learning Mode")
    st.markdown("- Emergency SOS Sign")
    st.markdown("- Custom Gesture Training (Coming soon)")

elif page == "Real-time Detection":
    st.header("🖐️ Real-time Bangla Sign Detection (Simulated)")
    uploaded_file = st.file_uploader("Upload an image of your hand sign", type=["jpg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Sign Image', use_column_width=True)
        with st.spinner("Detecting gesture..."):
            time.sleep(2)
            st.success("Detected sign: 'Ami Bhalo Achi' 🙌")
            st.audio("audio/ami_bhalo_achi.mp3")

elif page == "Text to Speech":
    st.header("📢 Bangla Text-to-Speech")
    text = st.text_input("Enter Bangla sentence:")
    if st.button("Convert to Voice"):
        tts = gTTS(text=text, lang='bn')
        tts.save("output.mp3")
        st.audio("output.mp3")

elif page == "Learn Signs":
    st.header("📘 Learn Bangla Sign Language")
    st.image("images/a_sign.jpg", caption="Sign for A", width=200)
    st.markdown("**Meaning**: A (অ) in Bangla")
    st.video("videos/sign_a.mp4")

elif page == "Emergency SOS":
    st.header("🚨 Emergency Gesture SOS")
    if st.button("Simulate SOS Gesture Detected"):
        st.error("⚠️ SOS Signal Sent!")
        st.write("Calling Guardian...")
        st.audio("audio/sos_call.mp3")
