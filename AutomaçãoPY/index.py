import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("Enter")

time.sleep(3)
pyautogui.click(x=505, y=434)
pyautogui.write("https://lightfill.xyz/")
pyautogui.press("Enter")

time.sleep(3)
pyautogui.click(x=1275, y=120)

time.sleep(3)
pyautogui.click(x=497, y=298)
pyautogui.write("Leo")
pyautogui.press("tab")
pyautogui.write("Souza")
pyautogui.press("tab")
pyautogui.write("leonadosanfelice@gmail.com")
pyautogui.press("tab")

time.sleep(3)
pyautogui.hotkey(x=713, y=400)
time.sleep(3)

pyautogui.write("Brazil")
pyautogui.click(x=763, y=443)
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.click(x=686, y=575)