import time
import random
import keyboard
import pyautogui
import threading

# Funtion to switch to Discord after launching the script. 
# Using pyautogui is honestly dumb 
def alt_tab():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('alt')

# Function to type "owoh" and hit enter
def type_owoh():
    alt_tab()
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

# Create two threads for the functions to run in
thread1 = threading.Thread(target=type_owoh)
thread2 = threading.Thread(target=type_owo_pray)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
