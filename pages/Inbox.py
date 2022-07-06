import streamlit as st

st.markdown('Some Ideas')
st.markdown("""

##### Update Main:

1. Play too high or low in pitch.
- Plan A: Comparing the user's recording with the sample piece and selecting the difference among them. Data are digitalized.
- Plan B: Using music21 to read the piece and generate the demo of the performance. Then, comparing the user's performance with music21's sample. (this can be a solution for tuner.)
2. Play too fast or slow for the rhythms.
- Idea: If the pitch of the note is change inthe next time step, note that as 1. Otherwise, note that as 0. Then, compare the 0/1 pattern to find out the rhythms is true or not.
- Problems: Can not detect the rhythms with the same notes in near time step.

##### Additional ideas to Main.

(3) Some basic information of sound/music:
- Reference:　Barry Parker, <Good Vibrations: The Physics of Music>, Johns Hopkins University Press, 2009-11-17, pp. 63[note's shape], 66-67[frequency].
- The same note sounds differently in shape with different instruments, for instant, violin and piano.
(4) Save Function 
- Recording & Report -> save them under user's account
(5) Tuner Function:
- Background beat counting with related speed, depended on the user's preference. 


##### Ideas with Streamlit:

(1) Adding animation:
- using Lottie in Streamlit and design a animation for AirMusic Icon/Logo. It can be an eye-catching image when user visit the webpage.

""")
