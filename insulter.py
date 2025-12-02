#INSTUCTIONS
#1. Fill in the insult variables with your desired insults.
#2. the time.sleep(X) controls the delay between insults, you can adjust it as needed.

import keyboard
import pyautogui
import random
import threading
import time

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.2

gooner = False

insult1 = "loser"
insult2 = "idiot"
insult3 = "cow"
insult4 = "moron"
insult5 = "stupid"

def start():
    global insult1, insult2, insult3, insult4, insult5

    while gooner:

       random1 = random.randint(1, 5)

       if random1 == 1:
          keyboard.write(insult1)
          pyautogui.press('enter')
       elif random1 == 2:
          keyboard.write(insult2)
          pyautogui.press('enter')
       elif random1 == 3:
          keyboard.write(insult3)
          pyautogui.press('enter')
       elif random1 == 4:
          keyboard.write(insult4)
          pyautogui.press('enter')
       elif random1 == 5:
           keyboard.write(insult5)
           pyautogui.press('enter')      
       time.sleep(0.8) #control delay here in seconds

def stop():
        print("stopping!")
        global gooner
        gooner = False        

def safeGuard():
    print("starting!")
    global gooner
    if not gooner:
        gooner = True
        threading.Thread(target=start, daemon=True).start()


keyboard.add_hotkey('shift+1', safeGuard)
keyboard.add_hotkey('esc', stop)

print("shift + 1 to start, esc to stop.")

while True:
    time.sleep(1)