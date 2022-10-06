# NOTE: Need the following libraries to make script run
#       speechRecognizer
#       pyaudio

import speech_recognition as sr
import pyaudio


print(sr.__version__)

r = sr.Recognizer()
myMic = sr.Microphone(device_index=0) # may be sensitive to system change


harvard = sr.AudioFile('testAudio/OSR_us_000_0010_8k.wav')
with harvard as source:
    audio = r.record(source)
print(type(audio))


#transcribe = r.recognize_google(audio)
#print(type(transcribe))
#print(transcribe)


#parsed = transcribe.split() # splits the string into a list of words

def fun():
    print("\n")

    with myMic as source:
        print("Say something!")
        audio = r.listen(source)

    voiceOutput = r.recognize_google(audio)
    print(voiceOutput.split())

    for i in voiceOutput.split():
        print(i)
    return voiceOutput

# How will it handle punctuation???
# NOTE: does not react to questions