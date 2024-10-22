import requests
import webbrowser
from threading import Thread
from random import choice
from os import startfile
import pyautogui

def block_mouse():
    while True:
        pyautogui.moveTo(0,0)

def generate_name():
    name = ""
    for i in range(10):
        name = name + choice(list("qwertyuiopasdfghjklzxcvbnm1234567890"))
    return name

def open_web():
    #while True:
    for i in range(10):
        webbrowser.open("https://cdn.pixabay.com/photo/2015/06/18/21/08/cat-814141_640.jpg")
def save_photo():
    # while True:
    for i in range(10):
        web_info = requests.get("https://cdn.pixabay.com/photo/2015/06/18/21/08/cat-814141_640.jpg")
        file_name = generate_name()
        img = open(f"C:\\Users\\LEGION\\Pictures\\Screenshots/{file_name}.jpg","wb")
        img.write(web_info.content)
        img.close()
        startfile(f"C:\\Users\\LEGION\\Pictures\\Screenshots/{file_name}.jpg")

print(generate_name())
pyautogui.FAILSAFE = False
block_mouse()
#open_web()
save_photo()