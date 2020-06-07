#!/usr/bin/env python3

import pyttsx3
import sys

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate
print ('Note: Setting speech to 150, previous:', rate) #printing current volume level

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
print ('Note: Setting volume to 1.0') #printing current volume level

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
print('Note: Number of voices available:', len(voices))
print('Note: Using english-us voice')
engine.setProperty('voice', 'english-us')

def speak(text):
  engine.say(text)
  engine.runAndWait() 

if len(sys.argv) == 2:
  speak(sys.argv[1])
else: 
  print('Usage: tts.py "Some words"')
  speak('You did not tell me what to say.')
  
