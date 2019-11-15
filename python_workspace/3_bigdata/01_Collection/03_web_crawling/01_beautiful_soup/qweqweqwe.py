import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
print(r.recognize_google(audio,language='ko-KR'))
import speech_recognition as sr
sr.__version__

r = sr.Recognizer():Google Web Speech API

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
    type(audio)

type(audio)
<class 'speech_recognition.AudioData'>


r.recognize_google(audio)

with harvard as source:
    audio1 = r.record(source, duration=4)
    audio2 = r.record(source, duration=4)


r.recognize_google(audio1)
r.recognize_google(audio2)

with harvard as source:
    audio = r.record(source, offset=4, duration=3)
​
recognizer.recognize_google(audio)
