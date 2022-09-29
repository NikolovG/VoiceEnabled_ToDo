import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

harvard = sr.AudioFile('audio/OSR_us_000_0010_8k.wav')
with harvard as source:
    audio = r.record(source)

type(audio)

#print(r.recognize_google(audio))

transcribe = r.recognize_google(audio)
print(type(transcribe))

