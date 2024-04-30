import speech_recognition as sr
from dotenv import dotenv_values

config = dotenv_values(".env")

r = sr.Recognizer()

harvard = sr.AudioFile("harvard.wav")
mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)
    transcript = r.recognize_azure(audio, config["AZURE_SPEECH_KEY"], location="southeastasia")
    print(transcript)