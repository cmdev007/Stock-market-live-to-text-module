#!/bin/python

import speech_recognition as sr
import sys
import os
header = sys.stdin.buffer.read(78)
while(1):
    #data = sys.stdin.buffer.read(882000) #5 sec
    data = sys.stdin.buffer.read(3528000) #20 sec
    f = open("/tmp/inter.wav", "wb")
    f.write(header)
    f.write(data)
    f.close()
    os.system("ffmpeg -y -i /tmp/inter.wav -f wav /tmp/inter_f.wav 2> /dev/null")

    File="/tmp/inter_f.wav"
    AUDIO_FILE = File
    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        print("#######################################################################################")
        print("Recognizing Text...")
        Data=r.recognize_google(audio)
        file1 = open("textData.txt","a")#append mode
        file1.write(Data+" ")
        file1.close()
        print("#######################################################################################")
        print("The audio file contains: " + Data)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech  Recognition service; {0}".format(e))
