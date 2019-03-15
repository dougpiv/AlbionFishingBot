import keyboard
import pyautogui as auto

while True:
    if keyboard.is_pressed('`'):
        auto.press('backspace')
        for i in range(5):
            auto.typewrite("@Merp#7497 ", 0.0025)
            auto.press('enter')
