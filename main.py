import speech_recognition as sr
import os
from pydub.silence import split_on_silence
from pydub import AudioSegment

# in case you'r using Windows, this shit requires additional lib!
# AudioSegment.converter = r'my-install-dir\\ffmpeg_full_gyanbin\\ffmpeg.exe'

# create a speech recognition object
r = sr.Recognizer()

print("Speak for 5 seconds:")
# open the file
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=3)
    print("Done.")
    print("Recognizing...")
    # convert speech to text
    # text = r.recognize_google(audio_data, language="uk-UA")
    text = r.recognize_google(audio_data, language="ru-RU")
    print(text)