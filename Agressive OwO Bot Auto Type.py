import time
import keyboard
import random

# Function to type "owoh" and hit enter
def type_owoh():
    keyboard.write("owoh\n")
    time.sleep(0.1)  # Sleep for a short duration to ensure "owoh" is typed completely
    keyboard.press("enter")
    keyboard.release("enter")


def type_owob():
    keyboard.write("owob\n")
    time.sleep(0.1)  # Sleep for a short duration to ensure "owob" is typed completely
    keyboard.press("enter")
    keyboard.release("enter")


# Set a flag to track if "CTRL + F12" is pressed
stop_flag = False

# Function to stop the loop when "CTRL + F12" is pressed
def stop_loop():
    global stop_flag
    stop_flag = True

# Register the hotkey for "CTRL + F12" to call the stop_loop function
keyboard.add_hotkey("ctrl+f12", stop_loop)

# Loop to type "owoh" every 15-20 seconds, until "CTRL + F12" is pressed
while not stop_flag:
    type_owoh()
    time.sleep(random.randrange(1, 3))
    type_owob()
    time.sleep(random.randrange(15, 20))

# Unregister the hotkey before exiting
keyboard.remove_hotkey(stop_loop)



