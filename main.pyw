# last edited 3-3-2022
import threading, json, time, Windows, os, tendo, ctypes
from infi.systray import SysTrayIcon
from pynput import mouse, keyboard
from tendo import singleton

os.chdir(os.path.dirname(os.path.abspath(__file__))) # changing the working directory to the directory where the script is

try:
    Me = singleton.SingleInstance() # To prevent multiple instances from running at the same time
except tendo.singleton.SingleInstanceException:
	Windows.OpenStatsWindow() # BUG: I think this is better than nothing happening but this causes a minor bug which is that 2 stats windows can be opened at the same time. Like if this got executed and then the user clicked on "Show stats". Consider fixing it by somehow telling the already running script to show the stats window. I will be ignoring this bug for now.
	exit()

Lock = threading.Lock() # used later to prevent a race condition from occuring.

class VariablesClass():
	def __init__(self):
		try:
			with open("Data.json") as File: # read the data from the file and assign variables to it
				Data = json.loads(File.read())
				self.LeftMouseClicks = Data["Left Clicks"]
				self.RightMouseClicks = Data["Right Clicks"]
				self.MiddleMouseClicks = Data["Middle Clicks"]
				self.MouseScrolls = Data["Scrolls"]
				self.KeyPresses = Data["Key Presses"]
				self.Letters = Data["Letters"]
				# Need those variables so that I can throttle how many times it saves to the file
				self.LastLeftMouseClicksValue = self.LeftMouseClicks
				self.LastRightMouseClicksValue = self.RightMouseClicks
				self.LastMiddleMouseClicksValue = self.MiddleMouseClicks
				self.LastMouseScrollsValue = self.MouseScrolls
				self.LastKeyPressesValue = self.KeyPresses
			with open("Data.backup", "w") as File:
				File.write(json.dumps(Data, indent=4))
		except:
			with open("Data.backup") as File: # read the data from the file and assign variables to it
				Data = json.loads(File.read())
			with open("Data.json", "w") as File: # opening and writing data in the file
				File.write(json.dumps(Data, indent=4))
			with open("Data.json") as File: # read the data from the file and assign variables to it
				Data = json.loads(File.read())
				self.LeftMouseClicks = Data["Left Clicks"]
				self.RightMouseClicks = Data["Right Clicks"]
				self.MiddleMouseClicks = Data["Middle Clicks"]
				self.MouseScrolls = Data["Scrolls"]
				self.KeyPresses = Data["Key Presses"]
				self.Letters = Data["Letters"]
				# Need those variables so that I can throttle how many times it saves to the file
				self.LastLeftMouseClicksValue = self.LeftMouseClicks
				self.LastRightMouseClicksValue = self.RightMouseClicks
				self.LastMiddleMouseClicksValue = self.MiddleMouseClicks
				self.LastMouseScrollsValue = self.MouseScrolls
				self.LastKeyPressesValue = self.KeyPresses
			ctypes.windll.user32.MessageBoxW(0, u"Error: The save file seems corrupted. Loaded backup instead.", u"Error", 0) # used this instead of pysimplegui to prevent "RuntimeError: main thread is not in main loop" error
Variables = VariablesClass()

def Quit(systray):
	os._exit(1) # I have no idea what the heck this does but it terminates all the running threads which is what I need
# and apparently I need to have an int as an argument and idk whats the difference between each number but 1 worked so
# thats what I used.

def ShowStats(systray):
	Windows.OpenStatsWindow()

def Save():
	with Lock: # using lock here becuase this function is called from two different threads which can lead to a race condition
		with open("Data.json", "w") as File: # opening and writing data in the file
			Data = {}
			Data["Left Clicks"] = Variables.LeftMouseClicks
			Data["Right Clicks"] = Variables.RightMouseClicks
			Data["Middle Clicks"] = Variables.MiddleMouseClicks
			Data["Scrolls"] = Variables.MouseScrolls
			Data["Key Presses"] = Variables.KeyPresses
			Data["Letters"] = Variables.Letters
			File.write(json.dumps(Data, indent=4))

def InitializeMouse():
	def OnClick(x, y, button, pressed):
		if pressed:
			if button == button.left: # check if its a left click
				Variables.LeftMouseClicks += 1
				Variables.LastLeftMouseClicksValue = Variables.LeftMouseClicks
				Save()
			if button == button.right: # check if its a right click
				Variables.RightMouseClicks += 1
				Variables.LastRightMouseClicksValue = Variables.RightMouseClicks
				Save()
			if button == button.middle: # check if its a middle click
				Variables.MiddleMouseClicks += 1
				Variables.LastMiddleMouseClicksValue = Variables.MiddleMouseClicks
				Save()

	def OnScroll(x, y, dx, dy):
		Variables.MouseScrolls += 1
		Variables.LastMouseScrollsValue = Variables.MouseScrolls
		Save()

	with mouse.Listener(on_click=OnClick, on_scroll=OnScroll) as listener:
		listener.join()
	
def InitializeKeyboard():

	def OnRelease(key):

		Variables.KeyPresses += 1
		# determine if a letter has been pressed and increase the count for that specific letter
		key = str(key).lower()
		if len(key) == 3:
			if key[1].isalpha() and key[1] in Variables.Letters:
				Variables.Letters[key[1]] += 1

		Variables.LastKeyPressesValue = Variables.KeyPresses # hold a key for a while it will register multiple key presses but you
		Save() # can only release a key once after pressing it.

	with keyboard.Listener(on_release=OnRelease) as KeyboardListener:
		KeyboardListener.join()
# Launching the system tray
menu_options = (("Show Stats", None, ShowStats),)
systray = SysTrayIcon("icon.ico", "Whatpulse Alternative v9", menu_options, on_quit=Quit)
systray.start()

MouseThread = threading.Thread(target=InitializeMouse, args=()) # Create a thread for the mouse
KeyboardThread = threading.Thread(target=InitializeKeyboard, args=()) # Create a thread for the keyboard
# start both threads
MouseThread.start()
KeyboardThread.start()