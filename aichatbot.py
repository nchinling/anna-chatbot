import numpy as np
import speech_recognition as sr


class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic)
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("sorry, could not recognise")


if __name__ == "__main__":
    ai = ChatBot(name="Mimi")
    while True:
        ai.speech_to_text()
