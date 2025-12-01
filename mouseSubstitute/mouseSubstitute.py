import pyautogui
import time
import keyboard
import pprint

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

screenlenth, screenHeight = pyautogui.size()

scaledLenth = screenlenth / 200

scaledHeight = screenHeight / 100

scrollingScaledHeight = int(round(scaledHeight))

def moveMouseRight():

    pyautogui.moveRel(scaledLenth, 0)

def moveMouseLeft():

    pyautogui.moveRel(-scaledLenth, 0)

def moveMouseDown():

    pyautogui.moveRel(0, scaledHeight)

def moveMouseUp():
    
    pyautogui.moveRel(0, -scaledHeight)

def leftClick():

    pyautogui.click()

def rightClick():

    pyautogui.rightClick()

def middleClick():

    pyautogui.middleClick()

def scrollUp():

    pyautogui.scroll(scrollingScaledHeight)                

def scrollDown():

    pyautogui.scroll(-scrollingScaledHeight)

keyboard.add_hotkey('shift+d', moveMouseRight)
keyboard.add_hotkey('shift+a', moveMouseLeft)
keyboard.add_hotkey('shift+s', moveMouseDown)
keyboard.add_hotkey('shift+w', moveMouseUp)
keyboard.add_hotkey('shift+q', leftClick)
keyboard.add_hotkey('shift+e', rightClick)
keyboard.add_hotkey('shift+r', scrollUp)
keyboard.add_hotkey('shift+f', scrollDown)
keyboard.add_hotkey('shift+1', middleClick)

keyboard.add_hotkey('ctrl+d', moveMouseRight)
keyboard.add_hotkey('ctrl+a', moveMouseLeft)
keyboard.add_hotkey('ctrl+s', moveMouseDown)
keyboard.add_hotkey('ctrl+w', moveMouseUp)
keyboard.add_hotkey('ctrl+q', leftClick)
keyboard.add_hotkey('ctrl+e', rightClick)
keyboard.add_hotkey('ctrl+r', scrollUp)
keyboard.add_hotkey('ctrl+f', scrollDown)
keyboard.add_hotkey('ctrl+1', middleClick)

keyboard.add_hotkey('alt+d', moveMouseRight)
keyboard.add_hotkey('alt+a', moveMouseLeft)
keyboard.add_hotkey('alt+s', moveMouseDown)
keyboard.add_hotkey('alt+w', moveMouseUp)
keyboard.add_hotkey('alt+q', leftClick)
keyboard.add_hotkey('alt+e', rightClick)
keyboard.add_hotkey('alt+r', scrollUp)
keyboard.add_hotkey('alt+f', scrollDown)
keyboard.add_hotkey('alt+1', middleClick)

pprint.pprint("Welcome, this application can be used to temporarily substitute your mouse.")
pprint.pprint("Hold shift or alt or ctrl and then use the wasd keys to control your mouse while holding shift, alt or ctrl.")
pprint.pprint("While holding alt or shift or ctrl, press e to right click and q to left click.")
pprint.pprint("Press r to scroll up with scrolling wheel and f to scroll down, 1 to press middle mouse button key(while holding ctrl, shift or alt).")
pprint.pprint("IMPORTANT, most applications will ignore or glitch out if you try to scroll up or down while holding ctrl or shift so iddeally hold alt while using scroll whell.")
pprint.pprint("Or use an built in scroll bar in the application, you can also press middle mouse button to turn your cursor into some weird thing to allow scrolling.")

while True:

    time.sleep(1)
