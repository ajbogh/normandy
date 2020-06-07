#!/usr/bin/env python3

import shlex
import sys
import subprocess

def execute_command(commandStr):
  print('Executing command: ', commandStr)
  commandArr = shlex.split(commandStr)
  print("Running command:", *commandArr)
  p = subprocess.run(commandArr)
  print('command complete')
  return p
  
