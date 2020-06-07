#!/usr/bin/env python3

import sys
import json
from Levenshtein import distance
from .command_executor import execute_command

MIN_DISTANCE = 5

def interpret_command(utterance):
  closest_command_index = -1
  closest_dist = sys.maxsize
  with open('./config/commands.json') as command_file:
    data = json.load(command_file)
    if data['keyword'] not in utterance: 
      return 0
    for index, p in enumerate(data['commands']):
      dist1 = distance('{} {}'.format(data['keyword'], p['utterance']), utterance)
      dist2 = distance('{} {}'.format(p['utterance'], data['keyword']), utterance)
      utterance_dist = min( dist1, dist2 )
      if utterance_dist < closest_dist:
        closest_command_index = index
        closest_dist = utterance_dist
      
      # print('Subprocess options: '+p['subprocess_options'])
    if closest_dist > -1 and closest_dist < MIN_DISTANCE:
      command = data['commands'][closest_command_index]
      print('Closest command:', command['utterance'])
      print('Interpreted utterance: ' + utterance)
      print('Utterance: ' + command['utterance'])
      print('Command: ' + command['command'])
      return execute_command(command['command'])
    else:
      return 0