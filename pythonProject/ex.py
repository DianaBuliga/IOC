import speech_recognition as sr
import pyttsx3

# Initialize the recognizer

# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    # print("say something")
    engine.say(command)
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        # r.recognize(audio)
        print(r.recognize_google(audio))

SpeakText("SAy something")
