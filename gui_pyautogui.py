import pyautogui

print(pyautogui.size())                                                                               

#mutliple assignments

width, height = pyautogui.size()
print(width)
print(height)

print(pyautogui.position())

pyautogui.moveTo(20, 750, duration=7.6)

# to move the mouse relative to its current position
#pyautogui.moveRel(200, 0)

pyautogui.click(20, 750, duration=5.5)

pyautogui.moveTo(20, 700, duration=7.9)
pyautogui.click(20, 700, duration=4.3)
pyautogui.moveTo(55, 610, duration=0.5)
pyautogui.click(55, 610, duration=0.5)
pyautogui.click(55, 610, duration=0.5)

