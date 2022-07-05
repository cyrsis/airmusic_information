import streamlit as st


def main():
    st.markdown("## AirMusic - The Perfect Companion for Music Practice")
    st.markdown("""
Statement:
Learning music is a long journey, good practice habits are essential.

Thousands of students learn music everyday, and they all can benefit from developing enhanced practice techniques.

AirMusic uses AI and Algo to study music and help students identify if they -

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

Userinterface:
1, Choosing the users' instrument.
2, Click the START and then give a few preparatory beat (預備拍).
3, User can start playing the instrument.
4, Generate report for the performance.
- Adding the restart and stop buttoms during the performence.
- Adding enlarge function.

Report template:
- The name of the piece/song.
- Number of error notes (with ratio/percentage). 
- Ranking amount the overall users.
- Recommeding the practice pieces for the users' weaknesses (Detect the weaknesses?). 

What do the app going to test/pratice:
(1) For normal pieces:
- Testing the pitch and beat -> comparing the error between the samples and the users' recording.
- Using machine to generate the samples.

Method for (1):
- Normalizing the autio data
- Comparing the sound wave by subtracting the samples digitized data and the users' recording digitized data, then taking absolute value.
If the value is smaller then a critical value, accept it. Otherwise, point out the error note with red color.
- Denoise (adding the background noise to the samples or autoencoder (not perfer))

(2) For instruments examination/grading test:
- The users need to learn from the professional musicians samples.
- The comparasion samples come from professional musicians with repected to the different instruments.
Remark: The musicial notation (symbol) may cause additional error.

Method for (2):
- Comparing the sound wave by subtracting the samples digitized data and the users' recording digitized data, then taking absolute value.
If the value is smaller then a critical value, accept it. Otherwise, point out the error note with red color.
- Denoise (adding the background noise to the samples or autoencoder (not perfer))

REMARKS:
- Starting at a quiet environment. Assume these do not exist external noise.

""")


if __name__ == '__main__':
    main()
