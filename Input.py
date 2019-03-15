import time
from random import randint
import pyautogui as auto


# Casts Fishing Rod, Hopefully The Random Time Makes It Seem Realistic
def cast_rod():
    auto.mouseDown()
    time.sleep(randint(0, 5))
    auto.mouseUp()

def click():
    auto.click()

def hold():
    auto.mouseDown()

def release():
    auto.mouseUp()

def use_fishing_bait():
    auto.typewrite('1')
