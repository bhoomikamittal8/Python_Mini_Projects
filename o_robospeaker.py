import os
import pyttsx3

print("Welcome to RoboSpeaker created by Bhoomika Mittal")
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True :
    text_to_speak = input("What do you want me to Speak? ")
    speak(text_to_speak)
    if text_to_speak == 'bye':
        speak("Toodles! have a good day!")
        break

