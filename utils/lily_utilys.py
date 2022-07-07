import music21
import streamlit as st


def lily_show(music):
    st.image(str(music.write('lily.png')))
