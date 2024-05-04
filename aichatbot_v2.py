import os
from gtts import gTTS
import numpy as np
import speech_recognition as sr
import datetime


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
            self.text = "ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("sorry, could not recognise")

    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        # macbook->afplay or for windows use->start
        os.system("afplay res.mp3")
        os.remove("res.mp3")

    def wake_up(self, text):
        # return True
        return True if self.name.lower() in text.lower() else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')

    @staticmethod
    def age():
        start_date = datetime.datetime(2024, 5, 4)  # May 4th, 2024
        current_date = datetime.datetime.now()
        age_in_days = (current_date - start_date).days
        return f"The age in terms of days starting from my birthday on May 4th is: {age_in_days} days."


if __name__ == "__main__":
    ai = ChatBot(name="Anna")
    while True:
        ai.speech_to_text()
        # wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello, I am Anna, an Artificial Intelligent being. What can I do for you?"
        elif "time" in ai.text:
            res = ai.action_time()
        elif "old" in ai.text:
            res = ai.age()
        elif any(i in ai.text for i in ["thank", "thanks"]):
            res = np.random.choice(
                ["you're welcome!", "anytime!",
                 "no problem!", "cool!",
                 "I'm here if you need me!", "peace out!"])
        else:
            res = "Please call me if you need anything."
        ai.text_to_speech(res)
