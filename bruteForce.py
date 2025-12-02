import keyboard
import threading
import pyautogui
import time
import random
import string
import mouse


pyautogui.PAUSE =  0
pyautogui.FAILSAFE = False

print("Welcome to bruteforce.")
print("1 to start and right click to stop.")

bf = False

def bruteForce():

    print("Bruteforce started!")
    global bf

    while bf:
        bread = None
        randomizer = random.randint(1, 11)
        if randomizer <10:
            bread = 24
        else:
            bread = 100

        length = random.randint(1, bread)
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

        keyboard.write(password)
        pyautogui.press('enter')
        time.sleep(0.001)


def stopBruteForce():

    global bf

    bf = False
    print("Bruteforce stopped!")


def safeGuard():

    global bf

    if not bf:

        bf = True
        threading.Thread(target=bruteForce, daemon= True).start()

keyboard.add_hotkey('1', safeGuard)
mouse.on_right_click(stopBruteForce)

while True:
    time.sleep(1)