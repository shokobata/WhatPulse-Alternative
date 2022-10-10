import os, time, json
from sys import exit
from datetime import date

datevar = date.today()
todaydate = str(datevar)
with open('DailyData.json', encoding='utf8') as loaddate:
    myDict = json.load(loaddate)
    datescope = myDict["Date"]
    if todaydate != datescope: # If Date is not concurrent, Updates Date key to current and relaunches the Reset.py again to move to Else
        with open('DailyData.json', encoding='utf8') as datereset:
            myDictDate = json.load(datereset)
            myDictDate["Date"] = todaydate
        with open('DailyData.json', 'w') as datereset:
            datereset.write(json.dumps(myDictDate, indent=4))
        with open('DailyData.json', encoding='utf8') as resetfile:
            myDict = json.load(resetfile)
            myDict["Today's LClicks"] = 1
            myDict["Today's RClicks"] = 1
            myDict["Today's MClicks"] = 1
            myDict["Today's Scrolls"] = 1
            myDict["Today's KeyPress"] = 1
            myDict["Today's letter"]['a'] = 1
            myDict["Today's letter"]['b'] = 1
            myDict["Today's letter"]['c'] = 1
            myDict["Today's letter"]['d'] = 1
            myDict["Today's letter"]['e'] = 1
            myDict["Today's letter"]['f'] = 1
            myDict["Today's letter"]['g'] = 1
            myDict["Today's letter"]['h'] = 1
            myDict["Today's letter"]['i'] = 1
            myDict["Today's letter"]['j'] = 1
            myDict["Today's letter"]['k'] = 1
            myDict["Today's letter"]['l'] = 1
            myDict["Today's letter"]['m'] = 1
            myDict["Today's letter"]['n'] = 1
            myDict["Today's letter"]['o'] = 1
            myDict["Today's letter"]['p'] = 1
            myDict["Today's letter"]['q'] = 1
            myDict["Today's letter"]['r'] = 1
            myDict["Today's letter"]['s'] = 1
            myDict["Today's letter"]['t'] = 1
            myDict["Today's letter"]['u'] = 1
            myDict["Today's letter"]['v'] = 1
            myDict["Today's letter"]['w'] = 1
            myDict["Today's letter"]['x'] = 1
            myDict["Today's letter"]['y'] = 1
            myDict["Today's letter"]['z'] = 1
        with open('DailyData.json', 'w') as resetfile:
            resetfile.write(json.dumps(myDict, indent=4))
            print("WARNING! Daily file has been reset!\n Restarting WhatPulse Alternative")
            time.sleep(3)
            os.system("start cmd /c startmain.pyw")
            quit()
    else:    
        with open('DailyData.json', encoding='utf8') as resetfile:
            myDict = json.load(resetfile)
            myDict["Today's LClicks"] = 1
            myDict["Today's RClicks"] = 1
            myDict["Today's MClicks"] = 1
            myDict["Today's Scrolls"] = 1
            myDict["Today's KeyPress"] = 1
            myDict["Today's letter"]['a'] = 1
            myDict["Today's letter"]['b'] = 1
            myDict["Today's letter"]['c'] = 1
            myDict["Today's letter"]['d'] = 1
            myDict["Today's letter"]['e'] = 1
            myDict["Today's letter"]['f'] = 1
            myDict["Today's letter"]['g'] = 1
            myDict["Today's letter"]['h'] = 1
            myDict["Today's letter"]['i'] = 1
            myDict["Today's letter"]['j'] = 1
            myDict["Today's letter"]['k'] = 1
            myDict["Today's letter"]['l'] = 1
            myDict["Today's letter"]['m'] = 1
            myDict["Today's letter"]['n'] = 1
            myDict["Today's letter"]['o'] = 1
            myDict["Today's letter"]['p'] = 1
            myDict["Today's letter"]['q'] = 1
            myDict["Today's letter"]['r'] = 1
            myDict["Today's letter"]['s'] = 1
            myDict["Today's letter"]['t'] = 1
            myDict["Today's letter"]['u'] = 1
            myDict["Today's letter"]['v'] = 1
            myDict["Today's letter"]['w'] = 1
            myDict["Today's letter"]['x'] = 1
            myDict["Today's letter"]['y'] = 1
            myDict["Today's letter"]['z'] = 1
        with open('DailyData.json', 'w') as resetfile:
            resetfile.write(json.dumps(myDict, indent=4))
            print("WARNING! Daily file has been reset!\nRestarting WhatPulse Alternative")
            time.sleep(1)
            os.system("start cmd /c startmain.pyw")
            quit()
