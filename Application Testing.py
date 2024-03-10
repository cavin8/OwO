import time
import keyboard
import random
import tkinter as tk
from threading import Thread

# Function to type "owoh" and hit enter
def type_owoh():
    keyboard.write("owoh\n")
    time.sleep(0.1)  # Sleep for a short duration to ensure "owoh" is typed completely
    keyboard.press("enter")
    keyboard.release("enter")


# Function to type "owob" and hit enter
def type_owob():
    keyboard.write("owob\n")
    time.sleep(0.1)  # Sleep for a short duration to ensure "owob" is typed completely
    keyboard.press("enter")
    keyboard.release("enter")

# Function to start typing
def start_typing():
    # Disable start button and enable stop button
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    # Start the typing loop in a separate thread
    typing_thread = Thread(target=typing_loop)
    typing_thread.start()


def stop_typing():
    global stop_flag

    # Set the stop flag to stop the typing loop
    stop_flag = True

    # Disable stop button and enable start button
    stop_button.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)


def typing_loop():
    while not stop_flag:
        type_owoh()
        time.sleep(random.randrange(1, 3))
        type_owob()
        time.sleep(random.randrange(15, 66))


# Create the main window
window = tk.Tk()
window.title("Typing GUI")

# Create the start button
start_button = tk.Button(window, text="Start", command=start_typing)
start_button.pack(pady=10)

# Create the stop button
stop_button = tk.Button(window, text="Stop", command=stop_typing, state=tk.DISABLED)
stop_button.pack(pady=10)

# Set a flag to track if typing loop should stop
stop_flag = False

# Start the GUI event loop
window.mainloop()
