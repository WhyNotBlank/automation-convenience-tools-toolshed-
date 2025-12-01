import pyautogui
import time
import keyboard
import threading

ih = False

pyautogui.PAUSE =  0.002501
pyautogui.FAILSAFE = False

print("Welcome to the Autoclicker!")
print("Ctrl + 7 to start Autoclicker and ctrl + 8 to stop Autoclicker.")


def startAuto():
   print("Autoclicker started!")
   global ih

   while ih:
        pyautogui.mouseDown()
        pyautogui.mouseUp()

def stopAuto():
   global ih
   print("Autoclicker stopped!")
   ih = False


def safeGuard():
    global ih
    if not ih:
        ih = True
        threading.Thread(target=startAuto, daemon=True).start()

keyboard.add_hotkey('ctrl+7', safeGuard)
keyboard.add_hotkey('ctrl+8', stopAuto)

while True:
    time.sleep(1)
