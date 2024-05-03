import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('personal.wav')
with harvard as source:
    audio = r.record(source)

type(audio)
print(r.recognize_google(audio))
