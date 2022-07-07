import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="AirMusic ML-Core", page_icon="📊", initial_sidebar_state="expanded"
)

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'current {i+1} %')
    bar.progress(i + 1)

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


st.subheader("last Update: July 6, 2022 7:41 AM")
