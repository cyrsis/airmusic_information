import streamlit as st
from music21 import *

# Stream

s1 = stream.Stream()
s1.append(note.Note('E6', quarterLength=1.5))
s1.append(note.Note('A5', quarterLength=1.5))
s1.append(note.Note('C6', quarterLength=0.5))
s1.append(note.Note('D6', quarterLength=0.5))
s1.append(note.Note('E6', quarterLength=2))
s1.append(note.Note('A5', quarterLength=2))
s1.append(note.Note('C6', quarterLength=0.5))
s1.append(note.Note('D6', quarterLength=0.5))
s1.append(note.Note('B5', quarterLength=4))
for i in s1.notes:
    st.write(i.octave)

# play music

st.audio(s1.notes, )
