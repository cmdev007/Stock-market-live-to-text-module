#!/bin/python

import speech_recognition as sr
import sys

#def argParse():
argv = sys.argv
#return args

#args = argParse()
File=argv[-1]

AUDIO_FILE = (File) 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 
    audio = r.record(source)   
  
try: 
    Data=r.recognize_google(audio)
    file1 = open("textData.txt","a")#append mode 
    file1.write(Data+"\n") 
    file1.close()
    print("The audio file contains: " + r.recognize_google(audio)) 
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech  Recognition service; {0}".format(e))
