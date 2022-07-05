import torch
import streamlit as st

st.write(f"### PyTorch version: {torch.__version__}")
# Check PyTorch has access to MPS (Metal Performance Shader, Apple's GPU architecture)
st.write(f"Is MPS (Metal Performance Shader) built? {torch.backends.mps.is_built()}")
st.write(f"Is MPS available? {torch.backends.mps.is_available()}")
# Set the device
device = "mps" if torch.backends.mps.is_available() else "cpu"
st.write(f"Using device: {device}")

st.markdown('---')
