import streamlit as st

st.markdown('#### Some Ideas')
st.markdown("""

##### Update Main:

1. Play too high or low in pitch.
- Plan A: Comparing the user's recording with the sample piece and selecting the difference among them. Data are digitalized.

##### Victor -> So we plan to use mp3 to the pitch? or use the pitch result from the App?
##### Both resolution can work, which one is easier?
###### No sure the time use (and pressure) for mp3 convert to pitch notes. If time consuming is not high, second one maybe more acc.

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

(3) Get the improvement from the histogram (if the histogram shows the users whare get wrong)
   - Violin have 4 main string, G3, D4, A4, E5 string. If all of basic 3 continuous notes playing are too low or high in a string, for example, the notes in G3 are all go wrong...
   They are A3, B3, C4, it turns out that the positions of the users' hand may be wrong. It is the same for all main string. The hand is too near your body if the pitch is too high.
   - If the pitch of G3 is wrong, it means user need to tuning his/her string.
   - If the pitch of D4, A4, E5 is/are wrong, it means user "may" need to tuning his/her string. (Since D4, A4, E5 has another fingering)
   - Also take G3 string as an example, if A3 do not wrong with B3 wrong and C4 wrong (or even wrong more), it means that the users' wrist (手腕) may touch the violin neck (琴頸). It is the same for all main string.
   - If the notes higher that B5 always go wrong, it means that the shifting technique of users should be improve.
   - More suggestion can added, details here:
     https://www.sixmonthsrebellion.com/en/blog/posts/「小提琴」搞定這5個方法，小提琴音準沒問題！-「violin」get-these-5-methods-the-violin-pitch-is-no-problem！
     
For the musicautobot.music_transformer dataloader.py, the fastai.text.data has not class LMLabelList now.


""")

st.markdown('---')

st.markdown("""

##### Links for Music21 .show situation:
https://groups.google.com/g/music21list/c/wcUsuqvbpUQ
https://colab.research.google.com/drive/17Fql7pyK3xsO8KmZorvb1tBoPomidCPB#scrollTo=TxLlKkizXMMG

""")

st.markdown('last update 8/7 11:16')
