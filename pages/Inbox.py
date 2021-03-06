import streamlit as st

st.markdown('#### Some Ideas')
st.markdown("""

##### Update Main:

1. Play too high or low in pitch.
- Plan A: Comparing the user's recording with the sample piece and selecting the difference among them. Data are digitalized.

##### Victor give u  the pitch in time series format
-C# July 8, 2022 1:36 PM
-A July 8, 2022 1:36 PM

- Plan B: Using music21 to read the piece and generate the demo of the performance. 
- Then, comparing the user's performance with music21's sample. (this can be a solution for tuner.)
---

2. Play too fast or slow for the rhythms.
- Idea: If the pitch of the note is change in the next time step, note that as 1. Otherwise, note that as 0. Then, compare the 0/1 pattern to find out the rhythms is true or not.
- Problems: Can not detect the rhythms with the same notes in near time step.
- Reference: Music Rhythm Detection Algorithm Based on Multipath Search and Cluster Analysis, https://www.hindawi.com/journals/complexity/2021/5627626/#related-work

##### Victor -> if we token (crop) the song, can we compare the length?
###### Reply: we would like to ask whats 'length' is stand for, yet crop the song into parts can be easier to identify the length of rhythms, like tuplet. 


##### Additional ideas to Main.

(3) Some basic information of sound/music:
- Reference: Barry Parker, <Good Vibrations: The Physics of Music>, Johns Hopkins University Press, 2009-11-17, pp. 63[note's shape], 66-67[frequency].
- The same note sounds differently in shape with different instruments, for instant, violin and piano.
##### Victor->  All we can is the pitch & Rhythms for now
###### Reply: Undoubtedly.
   
(4) Save Function 
- Recording & Report -> save them under user's account

(5) Tuner Function:
- Background beat counting with related speed, depended on the user's preference. 
##### Victor-> Or use the App Tuner
###### Reply: It would be great if there is avaliable, and it is aim to help user to start well.

##### Ideas with Streamlit:

(1) Adding animation:
- using Lottie in Streamlit and design a animation for 
  AirMusic Icon/Logo. It can be an eye-catching image when user visit the webpage.
  ##### Victor : Streamlit is design for internal USE only, it was for us to demo ideas in data science way
  ###### Reply: we got it. This was what we had suggested before the progress/work started.  

##### Think more about how to do it.
(1) Parents want to know how quickly they master techniques.
(2) Offer gamification features that encourage learners to practise more.
 - Planned -> Would add it when we have scope
(3) Get the improvement from the histogram (if the histogram shows the users whare get wrong)
   - Violin have 4 main string, G3, D4, A4, E5 string. If all of basic 3 continuous notes playing are too low or high in a string, for example, the notes in G3 are all go wrong...
   They are A3, B3, C4, it turns out that the positions of the users' hand may be wrong. It is the same for all main string. The hand is too near your body if the pitch is too high.
   - If the pitch of G3 is wrong, it means user need to tuning his/her string.
   - If the pitch of D4, A4, E5 is/are wrong, it means user "may" need to tuning his/her string. (Since D4, A4, E5 has another fingering)
   - Also take G3 string as an example, if A3 do not wrong with B3 wrong and C4 wrong (or even wrong more), it means that the users' wrist (??????) may touch the violin neck (??????). It is the same for all main string.
   - If the notes higher that B5 always go wrong, it means that the shifting technique of users should be improve.
   - More suggestion can added, details here:
     https://www.sixmonthsrebellion.com/en/blog/posts/????????????????????????5???????????????????????????????????????-???violin???get-these-5-methods-the-violin-pitch-is-no-problem???
     
For the musicautobot.music_transformer dataloader.py, the fastai.text.data has not class LMLabelList now.

##### Victor: Sounds pretty good to me, try to demo it

(4) Slow down/accerlerate function
- When user want to change the speed of practice/grading test, for example, 1) slow down the speed for beginner to ensure the accuracy of pitch and rhythm and familiar the piece, or 2) accerlerate the speed when the user want to challenge his/herself.
- Idea: 
- situation 1) if the piece is progressed by time, expend or shorten the time-used of the piece. 
- situation 2) if the piece is progressed pitch by pitch, it would be more dificult. 
- Reference: AudioSegment. https://medium.com/prog-ramming-solutions/python-music-playback-speed-1x-2x-3x-change-without-chipmunk-effect-890eb10826c1



""")

st.markdown('---')

st.markdown("""

##### Links for Music21 .show() situation:
https://groups.google.com/g/music21list/c/wcUsuqvbpUQ
https://colab.research.google.com/drive/17Fql7pyK3xsO8KmZorvb1tBoPomidCPB#scrollTo=TxLlKkizXMMG

""")

st.markdown('---')

st.markdown("""

##### Measuring performance

1)	Assuming regular rhythm, then each note can be matched for accuracy of pitch-name and/or intonation. Intonation errors may be anywhere from one cent (1/100 of a semitone) to 99 cents (anything over 100 will be wrong pitch rather than poor intonation).
   
   - Using something like tuner. To measure how it apart away from true pitch. Quantified it. Value between two half is 100.
  
2)	If the score on-screen shows these two different errors with differently coloured circles around the wrong notes the user can quickly see which they need to improve (e.g. red = wrong pitch, yellow = bad tuning).

   - Using something like tuner. Just previous suggestion, if the Quantified value between the actual pitch and user's pitch < 100, then yellow. If >= 100, then red.
   
3)	If the player sets a metronome tempo, the app can presumably adjust its in-built tempo for the stored music, and track each note in real time; if the player simply plays and expects the app to respond when it works out the tempo, it may take some notes or bars before the results can be shown.

   - Generate music by midi with different speed ...
   
4)	If the player does not play with regular rhythm then the tempo is a minor problem! This situation creates real difficulties, I think, for the app accurately to track the errors of pitch, especially if the player misplays note-lengths and causes distortion to the number of notes per bar and number of bars altogether.
   
   - Easy to find out where the error happended, but hard to find out which type of error has happended...
   
5)	To assess rhythmic errors (ignoring pitch errors for now) the app has to recognise a ???right??? note played for too short or too long a duration. Also, if the player is simply badly out of time and cannot maintain steady pulse, the app needs to be abl to adjust in some way so it can make a valid response on the rhythmic accuracy.

   - is it difficult to track every rhythm, but some online examples have been found and it can be reference for the idea/method.
   - Reference: https://essentia.upf.edu/tutorial_rhythm_beatdetection.html
   - https://essentia.upf.edu/streaming_extractor_music.html

6)	Music notation programmes do often include a realtime play-in facility and interpret the player???s performance into notation which fits the set time-signature ??? maybe this is a clue to how to deal with this issue?
   
   - 

""")

st.markdown('last update 8/7 11:51')
