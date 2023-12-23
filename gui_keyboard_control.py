import pyautogui
# pyautogui.click(500, 500); pyautogui.typewrite("Hello World", interval=0.5)
pyautogui.click(200, 200); pyautogui.typewrite(['a', 'b', 'left', 'left', 'x', 'y'], interval=1.0)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.click(200, 200); pyautogui.hotkey('ctrl', 's') #press multiple keys at same time
