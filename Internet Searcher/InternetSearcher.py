import pyautogui
import time

screen_width, screen_height = pyautogui.size()
word = input("What do you want to search: ")

pyautogui.moveTo(517, 1052)
pyautogui.click()

pyautogui.moveTo(110, 11)
pyautogui.click()

pyautogui.moveTo(192, 45)
pyautogui.click()
pyautogui.press('backspace')  # Backspace
pyautogui.write(word)
pyautogui.press('enter')
