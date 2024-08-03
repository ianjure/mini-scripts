import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
import pyautogui
import time as t
import struct
import pvporcupine
import pyaudio
import winsound
import os
import sys
import openai
from AppOpener import run
from subprocess import Popen

API = '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'

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        command = ''

    return command


def jarvis_main():
    while True:
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            break
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            break
        if 'search' in command:
            person = command.replace('search', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
            break
        if 'joke' in command:
            talk(pyjokes.get_joke())
            break
        if 'dota' in command:
            talk('Opening Dota')
            Popen(['D://Steam//steam.exe'])
            t.sleep(6)
            Popen(['D://Steam//steamapps//common//dota 2 beta//game//bin//win64//dota2.exe'])
            break
        if 'messenger' in command:
            talk('Accessing Messenger')
            webbrowser.open('https://messenger.com')
            break
        if 'code' in command:
            talk('Opening Visual Studio Code')
            Popen(['D://Microsoft VS Code//Code.exe'])
            break
        if 'notebook' in command:
            talk('Accessing Jupyter Notebook')
            run('anaconda prompt anaconda')
            t.sleep(3)
            pyautogui.typewrite('jupyter notebook')
            pyautogui.typewrite(["enter"])
            break
        if 'shutdown' in command:
            talk('Device Shutting Down')
            os.system('shutdown /s /t 10')
            break
        if 'exit' in command:
            talk('Going Offline')
            t.sleep(1)
            sys.exit()
        if 'hey jarvis' in command:
            openai.api_key = API

            prompt = command.replace('hey jarvis', '')
            completions = openai.Completion.create(prompt=prompt,
                                        engine='text-davinci-002',
                                        max_tokens=100)
            completion = completions.choices[0].text
            talk(completion)
            break
        
        t.sleep(2)


def main():
    porcupine = None
    pa = None
    audio_stream = None

    print('JARVIS is ONLINE and READY!')
    winsound.Beep(200,100)
    winsound.Beep(400,200)
    winsound.Beep(600,300)

    try:
        porcupine = pvporcupine.create(keywords=['jarvis', 'computer'])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from('h' * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print('Hotword Detected...', end="")
                talk('Yes')
                jarvis_main()
                t.sleep(1)
                print('JARVIS is AWAITING your CALL...')
    finally:
        if porcupine is not None:
            porcupine.delete()
        
        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()

main()