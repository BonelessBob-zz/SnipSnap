import pyautogui
from PIL import ImageGrab, ImageOps, ImageEnhance, Image
import keyboard
import time
import pytesseract
import pyperclip
import os

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
# print(pytesseract.get_tesseract_version())

def beautify(text):
    lines = text.split("\n")
    beautyText = ""

    for l in range(len(lines)):
        beautyText += lines[l] + "\r\n"
    return beautyText

while True:
    try:
        if keyboard.is_pressed('ctrl+shift+1'):
            pos1x, pos1y = pyautogui.position()
            time.sleep(0.5)

        elif keyboard.is_pressed('ctrl+shift+2'):
            pos2x, pos2y = pyautogui.position()
            time.sleep(0.5)

        elif keyboard.is_pressed('ctrl+shift+3'):
            if pos1x and pos2x:
                img = ImageGrab.grab((pos1x, pos1y, pos2x, pos2y))
                img = img.resize((img.width+round(img.width/2), img.height+round(img.height/2)), Image.ANTIALIAS)
                img = ImageOps.grayscale(img)
                img = ImageEnhance.Contrast(img)
                img = img.enhance(4)
                img.save("img.png")
                text = pytesseract.image_to_string(Image.open("img.png"))
                text = beautify(text)
                pyperclip.copy(text)

            #   ================OUTPUT===================
                print(text)
                os.remove("img.png")

        else:
            pass
        time.sleep(0.1)
    except:
        continue

