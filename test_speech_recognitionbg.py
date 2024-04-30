import speech_recognition as sr
from dotenv import dotenv_values

r = sr.Recognizer()
m = sr.Microphone()
config = dotenv_values(".env")

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_azure(audio, config["AZURE_SPEECH_KEY"], location="southeastasia")

            print('You said: "{}"'.format(value[0]))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Azure Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass