#!/usr/bin/env python3

import sys
import json
from Levenshtein import distance
from .command_executor import execute_command

MIN_DISTANCE = 5

def interpret_command(utterance):
  closest_command_index = -1
  closest_dist = sys.maxsize
  with open('./config/config.json') as config_file:
    config = json.load(config_file)
    with open('./config/commands.json') as command_file:
      commands = json.load(command_file)
      if config['keyword'] not in utterance: 
        return 0
      for index, p in enumerate(commands):
        utterance_dist1 = distance('{} {}'.format(config['keyword'], p['utterance']), utterance)
        utterance_dist2 = distance(p['utterance'], utterance)
        utterance_dist = min(utterance_dist1, utterance_dist2)
        if utterance_dist < closest_dist:
          closest_command_index = index
          closest_dist = utterance_dist

      if closest_dist > -1 and closest_dist < MIN_DISTANCE:
        command = commands[closest_command_index]
        print('Closest command:', command['utterance'])
        print('Interpreted utterance: ' + utterance)
        print('Utterance: ' + command['utterance'])
        print('Command: ' + command['command'])
        return execute_command(command['command'])
      else:
        return 0