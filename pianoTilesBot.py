from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 - x:428 y:400
#Tile 2 - x:571 y:400
#Tile 3 - x:700 y:400
#Tile 4 - x:845 y:400

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(3)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(428, 600)[0] == 0:
        click(428, 600)
    if pyautogui.pixel(571, 600)[0] == 0:
        click(571, 600)
    if pyautogui.pixel(700, 600)[0] == 0:
        click(700, 600)
    if pyautogui.pixel(845, 600)[0] == 0:
        click(845, 600)