import time
import random
import keyboard
import pyautogui
import threading
from time import sleep



# Function to switch to Discord and open #bot in Bummer server after launching the script.
def switch_to_discord():
    pyautogui.keyDown('win')
    pyautogui.press('r')
    pyautogui.keyUp('win')
    sleep(.1)
    pyautogui.write('discord:https://discord.com/channels/802350640110108689/802350640323493959')
    sleep(.2)
    pyautogui.press('enter')
    sleep(2)

# Function to minimize the cmd prompt after launching the script.
def minimize_cmd():
    pyautogui.keyDown('win')
    pyautogui.press('down')
    pyautogui.keyUp('win')
    sleep(.05)

# Function to type "owoh" and hit enter - MAIN FUNCTION
def type_owoh():
    minimize_cmd()
    switch_to_discord()
    while True:
        keyboard.write("owoh")
        keyboard.press_and_release("enter")
        type_owob()
        time.sleep(random.randrange(15, 66)) # Sleep for 15 - 66 seconds

# Function to type "owob" and hit enter
def type_owob():
    time.sleep(random.randrange(1, 3)) # Sleep for 1 - 3 seconds
    keyboard.write("owob")
    keyboard.press_and_release("enter")

# Function to type "owo pray" and hit enter
def type_owo_pray():
    while True:
        time.sleep(random.randrange(300, 360)) # Sleep for 5 - 6 minutes
        keyboard.write("owo pray")
        keyboard.press_and_release("enter")


#Funtion to pause the script by pressing "CTRL + END"
def pause():
    while True:
        if keyboard.is_pressed('ctrl + end'):
            print("Paused")
            while True:
                if keyboard.is_pressed('ctrl + end'):
                    print("Unpaused")
                    break
                else:
                    pass
        else:
            pass

# Create two threads for the functions to run in
thread1 = threading.Thread(target=type_owoh)
thread2 = threading.Thread(target=type_owo_pray)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
