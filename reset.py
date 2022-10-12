# last edited 10-10-2022
import os, json
import PySimpleGUI as sg
from datetime import date
from re import sub as sub

def DailyShowCase():
    with open("DailyData.json") as File:  # read the data from the file and displays it in popup window;
        Data = json.loads(File.read())
        File.close()
        Foxtrot = Data["Today's Letters"]
        Charlie = (dict(sorted(Foxtrot.items(), key=lambda val: val[1], reverse=True)))
        Juliett = ("\n".join("{!r}: {!r},".format(k.upper(), v) for k, v in Charlie.items()))
        Tango = sub(",", "", Juliett)
        Letters = sub("'", "", Tango)
        sg.PopupScrolled("Today's\nLetters\nUsage", f"{Letters}", title="Letters' Statistics",
                         background_color="grey", grab_anywhere=True, no_titlebar=True, font=16, auto_close=True,
                         auto_close_duration=30,  size=(12, 15))

def ShowCase():
    with open("Data.json") as File:  # read the data from the file and displays it in pop window;
        Data = json.loads(File.read())
        File.close()
        Foxtrot = Data["Letters"]
        Charlie = (dict(sorted(Foxtrot.items(), key=lambda val: val[1], reverse=True)))
        Juliett = ("\n".join("{!r}: {!r},".format(k.upper(), v) for k, v in Charlie.items()))
        Tango = sub(",", "", Juliett)
        Letters = sub("'", "", Tango)
        sg.PopupScrolled("Lifetime\nLetters\nUsage", f"{Letters}", title="Letters' Statistics",
                         background_color="grey", grab_anywhere=True, no_titlebar=True, font=16, auto_close=True,
                         auto_close_duration=30, size=(12, 15))

def File():
    with open('DailyData.json', encoding='utf8') as resetfile:  # Evoked by 'Reset' button, resets all daily values;
        myDict = json.load(resetfile)
        myDict["Today's LClicks"] = 0
        myDict["Today's RClicks"] = 0
        myDict["Today's MClicks"] = 0
        myDict["Today's Scrolls"] = 0
        myDict["Today's KeyPress"] = 0
        myDict["Today's Letters"]['a'] = 0
        myDict["Today's Letters"]['b'] = 0
        myDict["Today's Letters"]['c'] = 0
        myDict["Today's Letters"]['d'] = 0
        myDict["Today's Letters"]['e'] = 0
        myDict["Today's Letters"]['f'] = 0
        myDict["Today's Letters"]['g'] = 0
        myDict["Today's Letters"]['h'] = 0
        myDict["Today's Letters"]['i'] = 0
        myDict["Today's Letters"]['j'] = 0
        myDict["Today's Letters"]['k'] = 0
        myDict["Today's Letters"]['l'] = 0
        myDict["Today's Letters"]['m'] = 0
        myDict["Today's Letters"]['n'] = 0
        myDict["Today's Letters"]['o'] = 0
        myDict["Today's Letters"]['p'] = 0
        myDict["Today's Letters"]['q'] = 0
        myDict["Today's Letters"]['r'] = 0
        myDict["Today's Letters"]['s'] = 0
        myDict["Today's Letters"]['t'] = 0
        myDict["Today's Letters"]['u'] = 0
        myDict["Today's Letters"]['v'] = 0
        myDict["Today's Letters"]['w'] = 0
        myDict["Today's Letters"]['x'] = 0
        myDict["Today's Letters"]['y'] = 0
        myDict["Today's Letters"]['z'] = 0
    with open('DailyData.json', 'w') as resetfile:
        resetfile.write(json.dumps(myDict, indent=4))
        resetfile.flush()
        resetfile.close()
        print("WARNING! Daily file has been reset!\nRestarting WhatPulse Alternative")
        os.startfile("main.pyw")


def DateAndFile():
    datevar = date.today()
    todaydate = str(datevar)
    with open('DailyData.json', encoding='utf8') as loaddate:
        myDict = json.load(loaddate)
        datescope = myDict["Date"]
        if todaydate != datescope: # If Date is not concurrent, Updates Date key to today and resets all daily values to 1;
            with open('DailyData.json', encoding='utf8') as datereset:
                myDictDate = json.load(datereset)
                myDictDate["Date"] = todaydate
            with open('DailyData.json', 'w') as datereset:
                datereset.write(json.dumps(myDictDate, indent=4))
                datereset.flush()
                datereset.close()
            File()
        else:
            File()




