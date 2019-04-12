import pyautogui

#relative to position

for i in range(2): #so this means it starts from its current position then moves to other locations on the computer.
    pyautogui.moveRel(100,0, duration=1)
    print(pyautogui.position())
    pyautogui.moveRel(0,100, duration=.25)
    print(pyautogui.position())
    pyautogui.moveRel(-100,0, duration=.25)
    print(pyautogui.position())
    pyautogui.moveRel(0,-345, duration=.25)
    print(pyautogui.position())