import pyautogui
import time
import random
import os
import sys

with open("spamtext.txt",'r') as fuf:
    text = fuf.read().splitlines()
    print(text)

time.sleep(5)
print("OKey Go")

for i in range(5):
    pyautogui.typewrite(random.choice(text))
    pyautogui.press('enter')
    time.sleep(0.001)

