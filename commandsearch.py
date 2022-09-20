import pyautogui as pya
from tkinter import Tk
import keyboard
import os

def copy_clipboard():
    root = Tk()     # Initialize tkinter
    root.withdraw() # hide the tkinter window
    pya.hotkey("ctrl", "c") # copy the text (simulating key strokes)
    clipboard = root.clipboard_get() # get the text from the clipboard
    return clipboard

def turnlistostring(listor):
    stringmini = ""
    for i in range (0,len(listor)):
        stringmini = stringmini + listor[i]
        if listor[i] != listor[-1]:
            stringmini = stringmini + "+"    
    return stringmini



while True:
    var=[]
    if keyboard.is_pressed('`'):
        var=copy_clipboard().split()
        x=turnlistostring(var)
        y= "start chrome.exe --new-window --target https://www.google.com/search?q="
        z=y+x
        print(x)
        os.system(f'cmd /c "{z}"')