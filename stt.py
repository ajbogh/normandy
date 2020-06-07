#!/usr/bin/env python3
import speech_recognition as sr
import sys
import os
import time
from lib.command_interpreter import interpret_command
import json

r = sr.Recognizer()
mic = sr.Microphone()

old_energy_threshold = -1
  
def listen(source):  
  global old_energy_threshold
  print('Listening...')
  audio = r.listen(source)

  # try recognizing the speech in the recording
  # if a RequestError or UnknownValueError exception is caught,
  #     update the response object accordingly
  try:
    with open('./config/config.json') as config_file:
      config = json.load(config_file)
      client_id = config['houndify']['client_id']
      client_key = config['houndify']['client_key']
      utterance = r.recognize_houndify(audio, client_id, client_key)
      # utterance = r.recognize_sphinx(audio)
      old_energy_threshold = r.energy_threshold
      r.energy_threshold = 10000
      print("Recognized:", utterance)
      print("Updated energy threshold from {} to {}".format(old_energy_threshold, r.energy_threshold))
      interpret_command(utterance)
  except sr.RequestError as e:
    # API was unreachable or unresponsive
    print("Error: API unavailable", e)
  except sr.UnknownValueError:
    # speech was unintelligible
    print("Unable to recognize speech")
  

def start():
  global old_energy_threshold
  try:
    with mic as source:
      r.adjust_for_ambient_noise(source, duration = 1)
      while True:
        listen(source)
  except KeyboardInterrupt:
    print('Interrupted by keyboard')
    try:
        sys.exit(1)
    except SystemExit:
        os._exit(1)
 
  

start()
