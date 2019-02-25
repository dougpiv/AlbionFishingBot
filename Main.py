import time
from random import randint

import AutoInput as auto
import ImageGrab as img

# Initialize Bot
print("Bot Starting Up, Good Luck")

while True:
    for i in range(10):

        auto.cast_rod()  # Cast Fishing Rod (AutoInput.py)

        # if(sound.matches):                              # Wait For Fish Bite Sound (AudioCompare.py)
        #    auto.click()                                # Click Once To Start Fishing (AutoInput.py)

        position = 0
        while True:  # While Fishing Bar Is On Screen
            position = img.get_position()

            if position == -1:  # Fishing is Over
                print('position is ', position, ' breaking')
                break

            if position < 120:
                print('position is ', position, ' moving right')
                auto.hold()  # Move Right
                time.sleep(randint(0, 1))

            if position > 120:
                print('position is ', position, ' moving left')
                auto.release()  # Move Left
                time.sleep(randint(0, 0.5))

    # Every 10 Times, Use A Fishing Bait
    # auto.use_fishing_bait()
