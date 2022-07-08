import ly.document
import ly.musicxml
import streamlit as st
from mingus.containers import Bar
from music21 import *
from pathlib import Path
import mingus.extra.lilypond as LilyPond
# pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
from utils.lily_utilys import lily_show

st.title("Grade 6 Course")
st.markdown('---')
st.markdown("##### Sonata in G 3rd")
audio_file = open('streamlit_data/SonatainG3rdmvt.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

# st.image(res, width = 800)

# txt = Path('streamlit_data/app_course/Concertino_in_D_Op15_3rd.mxl').read_text().encode('UTF-8')
d = ly.document.Document(r'''
\version "2.18.0"

music = \relative {
  \time 4/4
  \key d \minor
  d4 e f g
  a g f e
  d2
}

\score {
  \new Staff <<
    \music
  >>
}
''')

## Try to display the Music Sheet in here
s = converter.parse('streamlit_data/app_course/Concertino_in_D_Op15_3rd.mxl')
st.set_option('deprecation.showPyplotGlobalUse', False)
# st.image(str(s.write('lily.png')))
# lily_show(s)
# st.pyplot(s.show())

p = graph.plot.HistogramPitchSpace(s)
st.write("Histogram-PitchSpace-count")
st.set_option('deprecation.showPyplotGlobalUse', False)
fig = p.run()
st.pyplot(fig)

st.markdown('---')
st.markdown('### Inside of the XML')
st.text(Path('streamlit_data/app_course/Sonata_in_G_3rd_mvt.musicxml').read_text())
