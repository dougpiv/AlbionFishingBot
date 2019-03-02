import time
from random import randint

import keyboard

import AutoInput as auto
import ImageGrab as img

# Initialize Bot
print("Bot Starting Up, Good Luck")

while True:

    for i in range(10):

        # auto.cast_rod()  # Cast Fishing Rod (AutoInput.py)
        if keyboard.is_pressed('`'):
            while True:  # While Fishing Bar Is On Screen
                position = img.get_position()

                if position == -1:  # Fishing is Over
                    print('position is ', position, ' breaking')
                    break

                if position < 120:
                    print('position is ', position, ' moving right')
                    auto.hold()  # Move Right
                    time.sleep(randint(0, 1) / 2)

                if position > 120:
                    print('position is ', position, ' moving left')
                    auto.release()  # Move Left
                    time.sleep(randint(0, 1) / 2)

    # Every 10 Times, Use A Fishing Bait
    # auto.use_fishing_bait()
