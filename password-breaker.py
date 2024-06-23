import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz0123456789";

allchars = list(chars)

pwd = pyautogui.password("Enter a password: ")

sample_pwd = ""

while sample_pwd != pwd:
    sample_pwd = random.choices(allchars, k=len(pwd))
    
    if sample_pwd == list(pwd):
        print("The password is: "+"".join(sample_pwd))
        break
    