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
time.sleep(5)
pa.moveTo(800, 540, 0.3)
pa.click()
pa.hotkey('shift','m')
pa.hotkey('a','c','a','l','i','s','a','n','g')
pa.hotkey('shift','2')
pa.hotkey('2','0','2','0','3','0','2')
pa.hotkey('9','9','0')
pa.moveTo(800, 640, 0.3)
pa.click()