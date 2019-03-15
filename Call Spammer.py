import time

import keyboard
import pyautogui as auto

while True:
    if keyboard.is_pressed('`'):
        for i in range(10):
            auto.click(130, 350)
            time.sleep(1)
            auto.click(285, 950)
