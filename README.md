# Mimi AI Chatbot suite
There are three programmes in this suite. It uses the Speech Recognition library to recognise and convert audio files to text. The programmes created are based on the tutorial at [https://realpython.com/python-speech-recognition/](https://realpython.com/python-speech-recognition/). An excerpt from the tutorial:
'The first component of speech recognition is, of course, speech. Speech must be converted from physical sound to an electrical signal with a microphone, and then to digital data with an analog-to-digital converter. Once digitized, several models can be used to transcribe the audio to text.'

## Approach
To decode the speech into text, groups of vectors are matched to one or more phonemes—a fundamental unit of speech. This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.

## 1. aichatbot.py
AI chatbot named Anna. It uses Google's Text-to-speech service which translates text to audio. It currently responds to age, name and date prompts.  

## 2. transcribe.py
A programme that transcribes audio files in wav format to text format. 

## 3. guessword.py
A guess the word game where players speak into the microphone, which the programme is able to recognise and respond accordingly. 

