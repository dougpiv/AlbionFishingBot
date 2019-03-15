import keyboard

import ImageGrab as img
import Input as inp

# Initialize Bot
print("Bot Starting Up, Good Luck")

while True:

    for i in range(10):

        if keyboard.is_pressed('`'):

            while True:  # While Fishing Bar Is On Screen
                position = img.get_position()

                if position == -1:  # Fishing is Over
                    print('position is ', position, ' breaking')
                    inp.release()
                    break

                if position < 135:
                    print('position is ', position, ' moving right')
                    inp.hold()  # Move Right
                    # time.sleep(randint(0, 1) / 2)

                if position > 145:
                    print('position is ', position, ' moving left')
                    inp.release()  # Move Left
                    # time.sleep(randint(0, 1) / 2)

        # Every 10 Times, Use A Fishing Bait
        inp.use_fishing_bait()
