import pyautogui
import time
import random
import keyboard
import sys
import tkinter as tk
from tkinter import Label
import os

# Configuration settings
SWITCH_INTERVAL = 240  # Seconds between tab switches
ENABLE_MOUSE_MOVEMENT = True  # Enable/disable mouse movement
ENABLE_SCROLLING = True  # Enable/disable scrolling
SCROLL_STEPS = 10  # Number of Page Down presses before resetting to top
STOP_KEY_COMBO = 'ctrl+alt'  # Key combo to stop script
COUNTDOWN_TIME = 10  # Initial countdown for shutdown popup (seconds)

# Set pyautogui pause duration (ms) for each action
pyautogui.PAUSE = 0.5
# Enable fail-safe (move mouse to upper-left corner to stop)
pyautogui.FAILSAFE = True

# Global flag to control main loop
is_running = True
# Global flag to prevent multiple popups
popup_active = False

def create_shutdown_popup():
    """Create a popup window with a 10-second countdown for script shutdown."""
    global popup_active
    if popup_active:
        print("Popup already active, ignoring additional trigger.")
        return
    popup_active = True
    try:
        print("Creating shutdown popup...")
        root = tk.Tk()
        root.title("Countdown")
        root.overrideredirect(True)  # Remove window border
        root.attributes('-topmost', True)  # Keep on top
        root.configure(bg='black')

        # Set size and position to bottom-left corner
        window_width = 200
        window_height = 60
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Position in bottom-left corner
        x_position = 0
        y_position = screen_height - window_height
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Add the label
        label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="black")
        label.pack(expand=True)

        # Countdown logic with local variable
        countdown = COUNTDOWN_TIME
        def update_countdown():
            nonlocal countdown
            try:
                if countdown >= 0:
                    print(f"Countdown: {countdown}")
                    label.config(text=f"Countdown: {countdown}s")
                    countdown -= 1
                    root.update()  # Force Tkinter to process events
                    root.after(1000, update_countdown)
                else:
                    root.quit()  # Stop the Tkinter event loop
                    root.destroy()  # Destroy the window
                    print("Shutdown popup closed. Exiting script.")
                    os._exit(0)  # Forceful exit
            except Exception as e:
                print(f"Error in countdown: {e}")
                root.quit()
                root.destroy()
                os._exit(1)

        # Start the countdown
        update_countdown()
        root.mainloop()
    except Exception as e:
        print(f"Error creating shutdown popup: {e}")
        popup_active = False
        os._exit(1)

def simulate_activity():
    """Simulate user activity by switching Chrome tabs, moving mouse, and scrolling down."""
    global is_running
    screen_width, screen_height = pyautogui.size()  # Get screen dimensions
    scroll_count = 0  # Track number of Page Down presses
    try:
        print("Ensure Chrome is open and active with multiple tabs before continuing...")
        time.sleep(3)  # Initial delay to allow user to focus Chrome
        
        # Register Ctrl+Alt handler
        def on_stop_key():
            global is_running
            print("\nCtrl+Alt detected. Initiating shutdown with popup...")
            is_running = False  # Stop the main loop
            keyboard.unhook_all()  # Remove hotkeys to prevent re-triggering
            create_shutdown_popup()
        
        keyboard.add_hotkey(STOP_KEY_COMBO, on_stop_key)
        
        while is_running:
            # Switch tabs within Chrome (Ctrl+Tab)
            print("Switching tab...")
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(random.uniform(0.5, 2))  # Random delay to mimic human action
            
            # Optional mouse movement (ping-pong across screen)
            if ENABLE_MOUSE_MOVEMENT:
                print("Moving mouse...")
                new_x = random.randint(int(screen_width * 0.1), int(screen_width * 0.9))
                new_y = random.randint(int(screen_height * 0.1), int(screen_height * 0.9))
                pyautogui.moveTo(new_x, y=new_y, duration=random.uniform(0.5, 1.0))
            
            # Optional scrolling (Page Down for SCROLL_STEPS, then reset to top)
            if ENABLE_SCROLLING:
                if scroll_count >= SCROLL_STEPS:
                    print("Reached scroll limit. Resetting to top.")
                    pyautogui.press('home')  # Jump to top
                    time.sleep(0.5)
                    scroll_count = 0  # Reset counter
                print("Scrolling down...")
                pyautogui.press('pagedown')  # Scroll down
                time.sleep(0.5)
                scroll_count += 2
            
            # Wait for next switch
            time.sleep(SWITCH_INTERVAL)

    except KeyboardInterrupt:
        print("\nScript terminated by user (Ctrl+C).")
        keyboard.unhook_all()  # Clean up hotkey
        is_running = False
        os._exit(0)  # Forceful exit
    except Exception as e:
        print(f"Error in simulate_activity: {e}")
        keyboard.unhook_all()
        is_running = False
        os._exit(1)

if __name__ == "__main__":
    print("Starting Chrome tab switcher script...")
    print(f"Press '{STOP_KEY_COMBO}' to stop with countdown.")
    time.sleep(3)  # Initial delay to allow user to prepare
    simulate_activity()
