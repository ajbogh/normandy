#!/usr/bin/env bash

sudo apt update
sudo apt install python3-pip libpulse-dev libasound2-dev python3-pyaudio
python3 -m pip3 install --upgrade pip3 setuptools wheel

pip3 install pyttsx3
pip3 install SpeechRecognition
pip3 install pocketsphinx
pip3 install python-Levenshtein
pip3 install google-api-python-client