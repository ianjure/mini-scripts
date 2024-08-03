import pyautogui as pa
from subprocess import Popen
import os
import time


pa.hotkey('win','ctrl','right')
print('Created new desktop!')
os.system('start chrome "https://www.messenger.com"')
time.sleep(1)
os.system('start chrome "https://classroom.google.com"')
time.sleep(1)
os.system('start chrome "https://ustep.ustp.edu.ph"')
