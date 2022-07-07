import streamlit as st

st.markdown('#### Some Ideas')
st.markdown("""

##### Update Main:

1. Play too high or low in pitch.
- Plan A: Comparing the user's recording with the sample piece and selecting the difference among them. Data are digitalized.

##### Victor -> So we plan to use mp3 to the pitch? or use the pitch result from the App?
##### Both resolution can work, which one is easier?

- Plan B: Using music21 to read the piece and generate the demo of the performance. Then, comparing the user's performance with music21's sample. (this can be a solution for tuner.)
---

2. Play too fast or slow for the rhythms.
- Idea: If the pitch of the note is change inthe next time step, note that as 1. Otherwise, note that as 0. Then, compare the 0/1 pattern to find out the rhythms is true or not.
- Problems: Can not detect the rhythms with the same notes in near time step.

##### Victor -> if we token (crop) the song, can we compare the length?


##### Additional ideas to Main.

(3) Some basic information of sound/music:
- Reference: Barry Parker, <Good Vibrations: The Physics of Music>, Johns Hopkins University Press, 2009-11-17, pp. 63[note's shape], 66-67[frequency].
- The same note sounds differently in shape with different instruments, for instant, violin and piano.
##### Victor->  All we can is the pitch & Rhythms for now
   
(4) Save Function 
- Recording & Report -> save them under user's account

(5) Tuner Function:
- Background beat counting with related speed, depended on the user's preference. 
##### Victor-> Or use the App Tuner

##### Ideas with Streamlit:

(1) Adding animation:
- using Lottie in Streamlit and design a animation for 
  AirMusic Icon/Logo. It can be an eye-catching image when user visit the webpage.

##### Think more about how to do it.
(1) Parents want to know how quickly they master techniques.
(2) Offer gamification features that encourage learners to practise more.

For the musicautobot.music_transformer dataloader.py, the fastai.text.data has not class LMLabelList now.


""")

st.markdown('---')

st.markdown("""

##### Links for Music21 .show situation:
https://groups.google.com/g/music21list/c/wcUsuqvbpUQ
https://colab.research.google.com/drive/17Fql7pyK3xsO8KmZorvb1tBoPomidCPB#scrollTo=TxLlKkizXMMG

""")

st.markdown('last update 7/7 16:02')
