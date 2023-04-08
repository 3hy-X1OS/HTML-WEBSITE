import pyautogui
from pynput import keyboard
from plyer import notification
import time , os
def mov_pos(x,y):
    pyautogui.PAUSE = 0
    screen_width, screen_height = pyautogui.size()
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        return
    pyautogui.moveTo(x, y)
mov_pos(0, 0)
def on_press(key):
    try:
        if key == keyboard.Key.esc:
            on_release(key)
        elif key == keyboard.Key.down:
            x, y = pyautogui.position()
            mov_pos(x, y+5)
        elif key == keyboard.Key.up:
            x, y = pyautogui.position()
            mov_pos(x, y-5)
        elif key == keyboard.Key.left:
            x, y = pyautogui.position()
            mov_pos(x-5, y)
        elif key == keyboard.Key.right:
            x, y = pyautogui.position()
            mov_pos(x+5, y)
        elif key == keyboard.KeyCode(char=','):
            pyautogui.mouseDown(button='right')
        elif key == keyboard.KeyCode(char='.'):
            pyautogui.mouseDown(button='left')
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        try:
            listener.stop()
        except:
            pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
mov_pos(0, 0)
