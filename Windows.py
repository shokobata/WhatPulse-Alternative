# last edited 7-1-2023
import PySimpleGUI as sg
import json, time, threading, os, reset
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
            Upload = Data["Upload"]
            Download = Data["Download"]

        with open("DailyData.json") as DFile: # read the data from the file and assign variables to it
            DData = json.loads(DFile.read())
            DLeftMouseClicks = DData["Today's LClicks"]
            DRightMouseClicks = DData["Today's RClicks"]
            DMiddleMouseClicks = DData["Today's MClicks"]
            DMouseScrolls = DData["Today's Scrolls"]
            DKeyPresses = DData["Today's KeyPress"]
            DLetters = DData["Today's Letters"]

        # the layout of the window
        col1=[[sg.Image("Mouse.png")], 
                [sg.Text("Left Clicks: "+"{:,}".format(LeftMouseClicks), key="_LeftClicks_", size=(18,1))],
                [sg.Text("Right Clicks: "+"{:,}".format(RightMouseClicks), key="_RightClicks_", size=(18,1))],
                [sg.Text("Middle Clicks: "+"{:,}".format(MiddleMouseClicks), key="_MiddleClicks_", size=(18,1))],
                [sg.Text("Scrolls: "+"{:,}".format(MouseScrolls), key="_Scrolls_", size=(18,1))],
                [sg.Text("Today's LClicks: " + "{:,}".format(DLeftMouseClicks), key="_DLeftClicks_", size=(18, 1))],
                [sg.Text("Today's RClicks: " + "{:,}".format(DRightMouseClicks), key="_DRightClicks_", size=(18, 1))],
                [sg.Text("Today's MClicks: " + "{:,}".format(DMiddleMouseClicks), key="_DMiddleClicks_", size=(18, 1))],
                [sg.Text("Today's Scrolls: " + "{:,}".format(DMouseScrolls), key="_DScrolls_", size=(18, 1))]]
        col2=[ [sg.Image("Keyboard.png")],
                [sg.Text("Key Presses: "+"{:,}".format(KeyPresses), key="_KeyPresses_", size=(21,1))],
                [sg.Text("Most Pressed letter: "+max(Letters, key=Letters.get).upper(), key="_Letters_", size=(21,1))],
                [sg.Text("Today's KeyPress: "+"{:,}".format(DKeyPresses), key="_DKeyPresses_", size=(21,1))],
                [sg.Text("Today's letter: "+max(DLetters, key=DLetters.get).upper(), key="_DLetters_", size=(21,1))],
                [sg.Image("wifi.png")],
                [sg.Text("Total Download: " + "{:,}".format(Download) + "GB", key="_Download_", size=(18, 1))],
                [sg.Text("Total Upload: " + "{:,}".format(Upload) + "GB", key="_Upload_", size=(18, 1))]]


        layout = [
            [sg.Column(col1, element_justification='c', justification="center"), sg.Column(col2, element_justification='c', justification="center", pad=(0,0))]
        ]

        window = sg.Window('WhatPulse Alternative v12', layout, use_default_focus=False, finalize=True, icon="icon.ico") # showing the window

        def UpdateWindow():
            StartTime = time.time() # Initial time
            while True:
                if time.time() - StartTime >= .1 and StatsOpen: # Check if .1 seconds passed then update the window
                    StartTime = time.time() # Reset initial time
                    try:
                        with open("Data.json") as File: # read the data from the file and assign variables to it
                            Data = json.loads(File.read()) #BUG: This will sometimes error because it apparently finds the file empty possibly because the other script it writing to it. Fix by adding a try except statement or maybe making a module manage the saving?
                            File.close()
                            LeftMouseClicks = Data["Left Clicks"]
                            RightMouseClicks = Data["Right Clicks"]
                            MiddleMouseClicks = Data["Middle Clicks"]
                            MouseScrolls = Data["Scrolls"]
                            KeyPresses = Data["Key Presses"]
                            Letters = Data["Letters"]
                            Upload = Data["Upload"]
                            Download = Data["Download"]
                            
                    except json.JSONDecodeError:
                        pass

                    try:
                        with open("DailyData.json") as File: # read the data from the file and assign variables to it
                            DData = json.loads(File.read()) #BUG: This will sometimes error because it apparently finds the file empty possibly because the other script it writing to it. Fix by adding a try except statement or maybe making a module manage the saving?
                            File.close() # Added try and except statement so GUI won't freeze #comment by Misanthropik
                            DLeftMouseClicks = DData["Today's LClicks"]
                            DRightMouseClicks = DData["Today's RClicks"]
                            DMiddleMouseClicks = DData["Today's MClicks"]
                            DMouseScrolls = DData["Today's Scrolls"]
                            DLetters = DData["Today's Letters"]
                            DKeyPresses = DData["Today's KeyPress"]
                    except json.JSONDecodeError:
                        pass


                    # updating the window text
                    try: # Handling exceptions because I can't fix the errors permenantly
                        window["_KeyPresses_"].update("Key Presses: "+"{:,}".format(KeyPresses))
                        window["_LeftClicks_"].update("Left Clicks: "+"{:,}".format(LeftMouseClicks))
                        window["_MiddleClicks_"].update("Middle Clicks: "+"{:,}".format(MiddleMouseClicks))
                        window["_RightClicks_"].update("Right Clicks: "+"{:,}".format(RightMouseClicks))
                        window["_Scrolls_"].update("Scrolls: "+"{:,}".format(MouseScrolls))
                        window["_Letters_"].update("Most Pressed letter: "+max(Letters, key=Letters.get).upper())
                        window["_DKeyPresses_"].update("Today's KeyPress: " + "{:,}".format(DKeyPresses))
                        window["_DLeftClicks_"].update("Today's LClicks: "+"{:,}".format(DLeftMouseClicks))
                        window["_DMiddleClicks_"].update("Today's MClicks: "+"{:,}".format(DMiddleMouseClicks))
                        window["_DRightClicks_"].update("Today's RClicks: "+"{:,}".format(DRightMouseClicks))
                        window["_DScrolls_"].update("Today's Scrolls: "+"{:,}".format(DMouseScrolls))
                        window["_DLetters_"].update("Today's letter: "+max(DLetters, key=DLetters.get).upper())
                        window["_Download_"].update("Total Download: " + "{:,}".format(Download) + "GB")
                        window["_Upload_"].update("Total Upload: " + "{:,}".format(Upload) + "GB")
                    except NameError:
                        continue
                    except RuntimeError:
                        continue
                if StatsOpen == False:
                    break
                time.sleep(0.1) # making the loop run every .1 seconds or else lag

        UpdateWindowThread = threading.Thread(target=UpdateWindow, args=(), daemon=True) # tbh, I don't remember why I added the daemon argument but hey it works so I will just leave it as it is.
        UpdateWindowThread.start()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED: # check if the window is closed
                StatsOpen = False
                break

            # CONTINUE: the three following if statements are currently useless, I mistakenly deleted the code that makes it work. I plan to add
            # that feature later though.
            if event == 'Reset': # evokes reset.py to reset values when 'Reset' button is called.
                if sg.popup_yes_no("Reset Today's values?\nNote: will restart,\n         check systray",  title= "Reset") == 'Yes':
                    reset.ResetDailyData()
                    os._exit(1)
                StatsOpen = True
            if event == "Today's": # Displays Daily Letters stats;
                reset.DailyShowCase()
                StatsOpen = True
            if event == 'Lifetime':  # Display LIfetime Letters stats; 
                reset.ShowCase()
                StatsOpen = True



            
        window.close(); del window # "The delete helps with a problem multi-threaded application encounter where tkinter complains that
        # it is being called from the wrong thread (not the program's main thread)", I don't think it helped tho.