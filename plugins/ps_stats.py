#!/usr/bin/env python3

import psutil
import subprocess
import os

cpu_percent = psutil.cpu_percent(interval=1)
memory_obj = psutil.virtual_memory()
current_directory = os.getcwd()

feeling = "I'm feeling great"

if cpu_percent >= 25: 
  feeling = "I'm feeling ok"
if cpu_percent >= 50: 
  feeling = "I'm a little stressed"
if cpu_percent >= 75: 
  feeling = "I'm not feeling so hot"
if cpu_percent >= 85: 
  feeling = "Mr. Stark, I don't feel so good"

cpu_message = 'My CPU is running at {} {}'.format(str(int(cpu_percent)),  "percent")
memory_message = 'My memory is {} percent used'.format(psutil.virtual_memory().percent)

subprocess.run(['python3 tts.py "{}"'.format(feeling)], shell=True)
subprocess.run(['python3 tts.py "{}"'.format(cpu_message)], shell=True)
subprocess.run(['python3 tts.py "{}"'.format(memory_message)], shell=True)