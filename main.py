import streamlit as st
import pandas as pd
import time
from PIL import Image

st.set_page_config(
    page_title="AirMusic ML-Core", page_icon="📊", initial_sidebar_state="expanded"
)

perc = st.empty()
bar = st.progress(0)
for i in range(100):
    perc.text(f'current {i+1} %')
    bar.progress(i + 1)
    
time.sleep(1)
    
perc.empty()
bar.empty()

st.markdown("### AirMusic ")
st.markdown("###### The Perfect Companion for Music Practice ")
st.markdown('---')
st.markdown('#### Statement:')
st.markdown("""
Learning music is a long journey, good practice habits are essential.

Thousands of students learn music everyday, and they all can benefit from developing enhanced practice techniques.

**AirMusic** uses 
AI and Algo to study music and help students identify if they -


play too high or too low in pitch;
play too fast or too slow for the rhythms;
or make errors which don’t make good musical sense.

The app. targets many standard set exam. pieces, for example Grades 3, 5 and 8 for violin and other instruments.

Simply click start and play, and your results are returned instantly. 

Features:
- Family report for parents;
    point out the error note with red color.
- Opera Track reports for multiple instruments;
    
- Special Read-out notes function for eyesight impaired users.
    Enlargement function

##### User Interface:
1. Choosing the users' instrument.
2. Click the 'START' and then give a few preparatory beat (預備拍).
3. User can start playing the instrument.
4. Generate report for the performance.

- Adding the restart and stop buttons during the performance.
- Adding enlarge function.

#####  Report template:
- The name of the piece/song.
- Number of error notes (with ratio/percentage). 
- Ranking amount the overall users (a. cheating cases excluded. b. ranking upload will be optional.).
- Recommending the practice pieces for the users' weaknesses (Detect the weaknesses?). 

##### What do the app going to test/practice:
##### (1) For normal pieces:
- Testing the pitch and beat -> comparing the error between the samples and the users' recording.
- Using machine to generate the samples.

##### Method for (1):
- Normalizing the audio data. Detect the outliers, then reject them from the normalized stat.
- Comparing the sound wave by subtracting the samples digitized data and the users' recording digitized data, then taking absolute value. 
- If the value is smaller then a critical value (will be adjusted for better result), accept it. Otherwise, point out the error note with red color.
- Denoise (adding the background noise to the samples or autoencoder (not prfer))

##### (2) For instruments examination/grading test:
- The users need to learn from the professional musicians samples.
- The comparison samples come from professional musicians with respected to the different instruments.

> Remark: The musical notation (symbol) may cause additional error.

##### Method for (2):
- Normalizing the audio data. Detect the outliers, then reject them from the normalized stat.
- Comparing the sound wave by subtracting the samples digitized data and the users' recording digitized data, then taking absolute value.
- If the value is smaller then a critical value (will be adjusted for better result), accept it. Otherwise, point out the error note with red color.
- Denoise (adding the background noise to the samples or autoencoder (not prefer))

##### Other factors
- The qualities of different instruments will produce different outputs (e.g. pitch).
- Determining the rhythms of the performance in the report. Testing will be, for instant, in every half-second (might be adjust for better result). 

> REMARKS:

- Starting at a quiet environment. Assume these do not exist external noise.
- All calculations and testings may not be confirmed before the demo. 

""")

st.markdown('---')

st.markdown("""
                        
##### Summarizing PitchDeck

The user plays their musical instrument to Air Music App according to the **displayed music scores** and the App will produce **an instant report analysing pitch and rhythm**, **pinpointing on the music exact errors and areas for improvement**. It includes 1. text prompt and 2. voice-over features (in different languages in the future): this important feature will particularly assist users with special needs.

With results accumulated during each term, parents and prospective teachers will have a more precise guide for school entry, and students can progress more confidently to higher grades with confirmed, reliable technical assurance. Air Music App can **inspire effective practice**, **provide an energising spur to practise**, and **lead to enhanced learning and growth in self-confidence**; families will know more certainly when the student is ready for the next grade exam. and which level to tackle next - leading to **a welcome reduction in over-ambitious teacher & parent expectations**. This will **train better practice habits**, **develop self-awareness of how to learn, what to listen for and how to listen, even, maybe, how to teach better**; and parents can check the teacher is doing the right things.

Air Music App will help learners:

- track progress

- highlight areas for improvement

- offer gamification features [1]  

it can encourage learners to practise more, at a readily affordable amount for any average music learner. Hong Kong alone has more than 1M music learners; it will therefore only take 2% of these learners to subscribe to the App to deliver a decent ROI.

Other Income:

Apart from ***regular fee income***, we will have music examination pieces and masterclasses performed by renowned educators. Examination repertoire can be included for more advanced learners. Thus, ***learners will pay subscriptions on a per-piece or per-grade basis***, while ***masterclasses will collect an annual subscription***.

Air Music App can also be ***tailor-made*** [2] to schools’ requirements, such as student orchestras and choirs, where conductors can monitor the performing quality of each player and singer using our App; since every school has an orchestra or choir - often both - and most of them compete regularly in the annual School Speech and Music Festivals. Our App will help extensively, particularly during and after COVID with the consequent knock-on online educational developments.

Additional future features will cover ***Chinese instruments*** [3] and learners. There is a huge free classical music database which we can match with the examination board requirements in the US, Canada, and China.

The ***community of music learners*** [4] offers significant 1. cross-selling opportunities with concert and event organisers, 2. music instrument and music score merchants and distributors, and 3. music education and entertainment institutions.

Air Music App is **“The Smartest AI for Effective Music Practice”**.

Remarks:

[1] Gamification features will be discuss after the app is done and the efficiency of the app is high enough. Otherwise, gamification features may cause time-consumed situation.

[2] Idea: serivce for a specific instrument (violin, piano, flute...) or orchestras and choirs as a whole.

[3] It is necessary to study the differences between Western instrument and Chinese instrument, depend on the sound waves and amplitudes produced are independent or not. Then, new database might need to build.

[4] It is hard to create until the app is familiar in the market and amount of users are using it. Community cannot be achieve in the current stage.

""")


st.subheader("last Update: July 7, 2022 15:06")
