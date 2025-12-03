import time
import random
import keyboard
import os

def main():

    random1 = random.randint(1, 3)
    random2 = random.randint(1, 3)

    adjective1 = None
    adjective2 = None
    noun1 = None
    noun2 = None
    verb1 = None
    verb2 = None

    if random1 == 1:

        print("=" * 15)
        adjective1 = input("Enter an adjective:")

    if random1 == 2:
        
        print("=" * 15)
        noun1 = input("Enter a noun:")
    
    if random1 == 3:

        print("=" * 15)
        verb1 = input("Enter a verb:")
    
    if random2 == 1:

        print("=" * 15)
        adjective2 = input("Enter an adjective: ")
    
    if random2 == 2:

        print("=" * 15)
        noun2 = input("Enter a noun: ")
    
    if random2 == 3:

        print("=" * 15)
        verb2 = input("Enter a verb: ")
                        
    if random1 == 1 and random2 == 1:

        print("=" * 15)
        print(f"The {adjective1} fox falls over the {adjective2} man.")
    
    if random1 == 1 and random2 == 2:

        print("=" * 15)
        print(f"The {adjective1} cop chases the {noun2}.")
    
    if random1 == 1 and random2 == 3:

        print("=" * 15)
        print(f"The {adjective1} human likes to {verb2}.")
    
    if random1 == 2 and random2 == 1:

        print("=" * 15)
        print(f"The {noun1} sleeps in the {adjective2} fence.")       
    
    if random1 == 2 and random2 == 2:
        
        print("=" * 15)
        print(f"The {noun1} brings a gift to the {noun2}.")
 
    if random1 == 2 and random2 == 3:

        print("=" * 15)
        print(f"The {noun1} decided to {verb2} today.")

    if random1 == 3 and random2 == 1:

        print("=" * 15)
        print(f"They {verb1} past the {adjective2} building.")

    if random1 == 3 and random2 == 2:    
        
        print("=" * 15)
        print(f"Robert likes to {verb1} with his {noun2}.")

    if random1 == 3 and random2 == 3:
        
        print("=" * 15)
        print(f"Every day they {verb1} and then {verb2}.")

def quit():

    print("=" * 15) 
    cow = input(f"Are you sure you want to quit? If yes then type 'yes' in all lowercase: ")
   
    if cow == "yes":
       
       print("=" * 15)
       print("Quitting...")
        
       os._exit(0)

    else:
        
        print("=" * 15)        
        #look behind
        print("It does not look like you wanted to quit. Press 'ctrl' to play again or 'esc' to quit.") 

print("Welcome to madlibs!")
print("Press 'ctrl' to start playing!")
print("You can play multiple times!")
print("Press 'esc' to quit.")

keyboard.add_hotkey('esc', quit)
keyboard.add_hotkey('ctrl', main)

while True:

    time.sleep(1)