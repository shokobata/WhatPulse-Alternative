# WhatPulse-Alternative

This will probably be badly written and formatted cuz I have no idea how this works. Hopefully I will improve it later.

My goal with this is to make a program with the same or nearly the same functionality as a program called WhatPulse. It should monitor your inputs anywhere except if you are using a program with administrator privelages such as genshin impact.

The features that WhatPulse Alternative currently have are:
* Monitoring the number of keyboard presses
* Monitoring the number of left clicks
* Monitoring the number of right clicks
* Monitoring the number of middle mouse button clicks
* Monitoring the number of scrolls (Each click when using the scroll wheel)
* Monitoring the most used keyboard letter
* Monitoring of daily metrics separate from lifetime.
* Manual reset function for daily metrics (it'll automatically reset on next date regardless)
* A GUI to display all of the data mentioned above
* A backup system

**Installation Instructions:**
- Download and install python. Make sure to check the box that says "add python 3.x to PATH" before installing.
- Download all the files by clicking on the green button labeled "Code" and then clicking on "Download ZIP".
- Unzip the download zip file in the folder where you want the program to be.
- Delete "README.md" because it is useless now.
- Open the command prompt in the folder where your downloaded files are and then run the following command: `pip install -r requirements.txt`.
- Now you are basically done. You can run the "main.py" file for the program to run. **Only follow the next steps if you want the program to run on startup**, in other words, if you want the program to run everytime your computers is turned on.
- Right click on the "main.pyw" file and click on "Create shortcut".
- Press the windows key and r simultaneously. The run window will popup. Type `shell:startup` and press enter. Finally, put the "main.pyw" shortcut you created earlier in the startup folder that you just opened using the run window.

**Usage Guide:**
When the program runs it adds itself to the system tray (that thing on the bottom right of your screen where steam or other game launchers run there). All you need to do is double click it or right click then choose "Show Stats". After that, a window will open showing all of your stats. Closing the stats window will not close the program itself. The program will stay working in the background. To stop the program from running, right click on it from the system tray and choose "Quit".

**Warning:** Daily metrics will reset everyday, CMD dialogs will pop up for couple of seconds during midnight hours to let you know or first boot of the next day or when clicking the 'Reset" button in the GUI. You can remove the time.sleep() line in reset.py to reduce delay.

**Known Issues:**
- Lagging when opening the stats window for the first time.
- 2 bugs (Check code for more info about them)
