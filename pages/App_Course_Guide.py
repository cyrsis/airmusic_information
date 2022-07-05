import streamlit as st
from pathlib import Path

# pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

st.title("Grade 6 Course")
audio_file = open('streamlit_data/SonatainG3rdmvt.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')
# st.image(res, width = 800)
