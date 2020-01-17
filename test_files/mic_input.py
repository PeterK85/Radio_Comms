import speech_recognition as sr
#import sphinxbase
import pocketsphinx

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    print("time up")

try:
    print("text: "+r.recognize_sphinx(audio));
except sr.UnknownValueError:
    print("UNknown value error")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    pass;
