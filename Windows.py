# last edited 4-2-2022
import PySimpleGUI as sg
import json

sg.theme('DarkAmber')

StatsOpen = False

def StartStatsWindow():
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

        # the layout of the window
        col1=[[sg.Image("Mouse.png")], 
                [sg.Text("Left Clicks: "+str(LeftMouseClicks), key="_LeftClicks_", size=(18,1))],
                [sg.Text("Right Clicks: "+str(RightMouseClicks), key="_RightClicks_", size=(18,1))],
                [sg.Text("Middle Clicks: "+str(MiddleMouseClicks), key="_MiddleClicks_", size=(18,1))],
                [sg.Text("Scrolls: "+str(MouseScrolls), key="_Scrolls_", size=(18,1))]]
        col2=[ [sg.Image("Keyboard.png")],
                [sg.Text("Key Presses: "+str(KeyPresses), key="_KeyPresses_", size=(18,1))],
                [sg.Button('Refresh')]]

        layout = [
            [sg.Column(col1, element_justification='c', justification="center"), sg.Column(col2, element_justification='c', justification="center")]
        ]

        window = sg.Window('WhatPulse Alternative', layout, use_default_focus=False) # showing the window

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED: # check if the window is closed
                StatsOpen = False
                break
            if event == "Refresh": # check if the refresh button is pressed
                with open("Data.json") as File: # read the data from the file and assign variables to it
                    Data = json.loads(File.read())
                    LeftMouseClicks = Data["Left Clicks"]
                    RightMouseClicks = Data["Right Clicks"]
                    MiddleMouseClicks = Data["Middle Clicks"]
                    MouseScrolls = Data["Scrolls"]
                    KeyPresses = Data["Key Presses"]
                # updating the window text
                window["_KeyPresses_"].update("Key Presses: "+str(KeyPresses)) 
                window["_LeftClicks_"].update("Left Clicks: "+str(LeftMouseClicks))
                window["_MiddleClicks_"].update("Middle Clicks: "+str(MiddleMouseClicks))
                window["_RightClicks_"].update("Right Clicks: "+str(RightMouseClicks))
                window["_Scrolls_"].update("Scrolls: "+str(MouseScrolls))
            
        window.close()
