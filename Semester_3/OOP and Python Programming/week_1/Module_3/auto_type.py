import pyautogui
from time import *
sleep(10)

for i in range(0, 4):
    pyautogui.write("Hello Programmers", interval=0.25)
    pyautogui.press("enter")
