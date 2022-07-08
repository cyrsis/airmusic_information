from pathlib import Path

import streamlit as st

st.markdown(Path('README.md').read_text())
