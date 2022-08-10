import pyautogui
import time
while True:
    pyautogui.moveRel(100, 0)
    time.sleep(60)
    pyautogui.moveRel(0, 100)
    time.sleep(60)
    pyautogui.moveRel(-100, 0)
    time.sleep(60)
    pyautogui.moveRel(0, -100)
    time.sleep(60)
