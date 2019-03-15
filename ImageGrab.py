import time
import cv2
import numpy as np
from PIL import ImageGrab


# Example Pulled From Code Bullet Videos
def screen_record():
    last_time = time.time()
    while True:
        print_screen = np.array(ImageGrab.grab(bbox=(839, 538, 1080, 566)))  # Left, Upper, Right, Lower
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        cv2.imshow('Fishing Capture', cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def get_position():  # Captures Image, Then Iterates Until It Finds A White Pixel
    capture = ImageGrab.grab(bbox=(839, 550, 1080, 551))  # Left, Upper, Right, Lower
    threshold = 150
    fn = lambda x: 255 if x > threshold else 0
    nums = np.array(capture.convert('L').point(fn, mode='1')).astype(int)

    for (x, y), value in np.ndenumerate(nums):
        if value == 1:
            return y + 7  # In This Case, 14 Is The Length Of The Marker So 7 Is The Middle
    return -1


def is_fishing():  # Captures Most Of The Screen
    capture = np.array(ImageGrab.grab(bbox=(262, 140, 1578, 963)))
