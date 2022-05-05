from email.mime import audio
from unittest import result
import speech_recognition as sr
import moviepy.editor as mp

#       ****** vedio to mp3 and mp3 to text ****** 
clip = mp.VideoFileClip(r"microsoft.mp4") #specify the correct file path to your video file 

# Apne app convert krdega
clip.audio.write_audiofile(r"converted_mp3.wav") #this the name of the coverted audio file


r = sr.Recognizer()
audio=sr.AudioFile(r"converted_mp3.wav")
with audio as source:
    audio_file = r.record(source)

result = r.recognize_google(audio_file)

with open('recog.txt',mode='w') as file:
    file.write("speech recognized")
    file.write("\n")
    file.write(result)
    print("Now the file is ready")