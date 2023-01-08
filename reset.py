# Last modified: 4-1-2023
import os
import json
import PySimpleGUI as sg
from datetime import date
from string import ascii_lowercase

def DailyShowCase(): # CONTINUE: This function is currently useless. I plan to use it gain later on
    """read data from DailyData.json and display it in a popup window"""

    with open("DailyData.json") as f:  # 
        Data = json.load(f)

    Letters = Data["Today's Letters"]
    SortedLetters = dict(sorted(Letters.items(), key=lambda val: val[1], reverse=True))
    FinalString = ("\n".join(f"{k.upper()}: {v}" for k, v in SortedLetters.items()))

    sg.PopupScrolled("Today's\nKeystrokes", f"{FinalString}", title="Keystroke Statistics",
                     background_color="grey", grab_anywhere=True, no_titlebar=True, font=16, auto_close=True,
                     auto_close_duration=30,  size=(12, 15))


def ShowCase(): # CONTINUE: This function is currently useless. I plan to use it gain later on
    """read data from Data.json and display it in a popup window"""

    with open("Data.json") as File:
        Data = json.load(File)

    Letters = Data["Letters"]
    SortedLetters = dict(sorted(Letters.items(), key=lambda val: val[1], reverse=True))
    FinalString = "\n".join(f"{k.upper()}: {v}" for k, v in SortedLetters.items())

    sg.PopupScrolled("Lifetime\nKeystrokes\n", f"{FinalString}", title="Keystroke Statistics",
                     background_color="grey", grab_anywhere=True, no_titlebar=True, font=16, auto_close=True,
                     auto_close_duration=30, size=(12, 15))


def ResetDailyData():
    """resets all daily values"""
    newData = {
        "Today's LClicks": 0,
        "Today's RClicks": 0,
        "Today's MClicks": 0,
        "Today's Scrolls": 0,
        "Today's KeyPress": 0,
        "Today's Letters": {},
        "Date": str(date.today())
    }

    for letter in ascii_lowercase:
        newData["Today's Letters"][letter] = 0

    with open('DailyData.json', 'w', encoding='utf8') as f:
        json.dump(newData, f, indent=4)