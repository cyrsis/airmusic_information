import streamlit as st
from mingus.containers import Bar
from music21 import *
from pathlib import Path
import mingus.extra.lilypond as LilyPond
# pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

st.title("Grade 6 Course")
st.markdown("##### Sonata in G 3rd")
audio_file = open('streamlit_data/SonatainG3rdmvt.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')
# st.image(res, width = 800)

# n = m21.note.Note('c')
# n.show('ipython.musicxml.png')

s = converter.parse('streamlit_data/app_course/ConcertinoinDOp15_3rd.mxl')
st.set_option('deprecation.showPyplotGlobalUse', False)
# st.write(s.show('ipython.musicxml.png'))
st.pyplot(s.show())

p = graph.plot.HistogramPitchSpace(s)
# p.id
st.write("Histogram-PitchSpace-count")
st.set_option('deprecation.showPyplotGlobalUse', False)
fig = p.run()
st.pyplot(fig)
