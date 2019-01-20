# !/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 1/20/19


import sys
import os
import webbrowser
import speech_recognition as sr


def talk(words):
    print(words)
    os.system('say ' + words)


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('speak')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source, duration=1)
        audio = r.listen(source)

    try:
        action = r.recognize_google(audio).lower()
        print(action)
    except sr.UnknownValueError:
        talk('something went wrong')
        action = command()

    return action


def makeTask(task):
    if 'open website' in task:
        talk('already opening...')
        url = 'https://google.com/'
        webbrowser.open(url)
    elif 'stop' in task:
        talk('bye')
        sys.exit()


if __name__ == '__main__':
    talk('hi, say something')
    while True:
        makeTask(command())