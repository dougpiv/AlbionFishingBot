import time

import keyboard

import Input as auto

while True:
    if keyboard.is_pressed('`'):
        auto.click()
        time.sleep(0.05)
