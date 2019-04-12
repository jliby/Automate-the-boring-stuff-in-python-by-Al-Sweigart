#! python3
# mouseNow.py - Displays the current position of the mouse on the screen.

import pyautogui
print('CTR-C to quit. If it gets out of hand buddy.')
#TODO - I need to print where the mouse is all the time.
try:
    while True:
        #TODO - print the whereabouts of the mouse
        #TODO - make it look nice.
        x ,y = pyautogui.position()
        positionString = 'X:' + str(x).rjust(4) + 'Y:' + str(y).rjust(4)
        print(positionString, end='')
        print('\b' * len(positionString), end='', flush=True)
except KeyboardInterrupt:
    print('\Done. Sorry if I got out of hand.')c