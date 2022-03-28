# last edited 3-3-2022
import PySimpleGUI as sg
import json, time, threading, os

sg.theme('DarkAmber')

StatsOpen = False

def OpenStatsWindow():
    global StatsOpen

    if StatsOpen == False: # check if the window is already open
        StatsOpen = True

        with open("Data.json") as File: # read the data from the file and assign variables to it
            Data = json.loads(File.read())
            LeftMouseClicks = Data["Left Clicks"]
            RightMouseClicks = Data["Right Clicks"]
            MiddleMouseClicks = Data["Middle Clicks"]
            MouseScrolls = Data["Scrolls"]
            KeyPresses = Data["Key Presses"]
            Letters = Data["Letters"]

        # the layout of the window
        col1=[[sg.Image("Mouse.png")], 
                [sg.Text("Left Clicks: "+"{:,}".format(LeftMouseClicks), key="_LeftClicks_", size=(18,1))],
                [sg.Text("Right Clicks: "+"{:,}".format(RightMouseClicks), key="_RightClicks_", size=(18,1))],
                [sg.Text("Middle Clicks: "+"{:,}".format(MiddleMouseClicks), key="_MiddleClicks_", size=(18,1))],
                [sg.Text("Scrolls: "+"{:,}".format(MouseScrolls), key="_Scrolls_", size=(18,1))]]
        col2=[ [sg.Image("Keyboard.png")],
                [sg.Text("Key Presses: "+"{:,}".format(KeyPresses), key="_KeyPresses_", size=(18,1))],
                [sg.Text("Most Pressed letter: "+max(Letters, key=Letters.get).upper(), key="_Letters_", size=(18,1))] ]

        layout = [
            [sg.Column(col1, element_justification='c', justification="center"), sg.Column(col2, element_justification='c', justification="center")]
        ]

        window = sg.Window('WhatPulse Alternative v9', layout, use_default_focus=False, finalize=True) # showing the window

        def UpdateWindow():
            StartTime = time.time() # Initial time
            while True:
                if time.time() - StartTime >= 1 and StatsOpen: # Check if 1 second passed then update the window
                    StartTime = time.time() # Reset initial time
                    with open("Data.json") as File: # read the data from the file and assign variables to it
                        Data = json.loads(File.read()) #BUG: This will sometimes error because it apparently finds the file empty possibly because the other script it writing to it. Fix by adding a try except statement or maybe making a module manage the saving?
                        LeftMouseClicks = Data["Left Clicks"]
                        RightMouseClicks = Data["Right Clicks"]
                        MiddleMouseClicks = Data["Middle Clicks"]
                        MouseScrolls = Data["Scrolls"]
                        KeyPresses = Data["Key Presses"]
                        Letters = Data["Letters"]
                    # updating the window text
                    try: # Handling exceptions because I can't fix the errors permenantly
                        window["_KeyPresses_"].update("Key Presses: "+"{:,}".format(KeyPresses)) 
                        window["_LeftClicks_"].update("Left Clicks: "+"{:,}".format(LeftMouseClicks))
                        window["_MiddleClicks_"].update("Middle Clicks: "+"{:,}".format(MiddleMouseClicks))
                        window["_RightClicks_"].update("Right Clicks: "+"{:,}".format(RightMouseClicks))
                        window["_Scrolls_"].update("Scrolls: "+"{:,}".format(MouseScrolls))
                        window["_Letters_"].update("Most Pressed letter: "+max(Letters, key=Letters.get).upper())
                    except NameError:
                        continue
                    except RuntimeError:
                        continue
                if StatsOpen == False:
                    break
                time.sleep(1) # making the loop run every second or else lag

        UpdateWindowThread = threading.Thread(target=UpdateWindow, args=(), daemon=True) # tbh, I don't remember why I added the daemon argument but hey it works so I will just leave it as it is.
        UpdateWindowThread.start()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED: # check if the window is closed
                StatsOpen = False
                break
            
        window.close(); del window # "The delete helps with a problem multi-threaded application encounter where tkinter complains that it is being called from the wrong thread (not the program's main thread)", I don't think it helped tho.