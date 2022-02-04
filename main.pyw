# last edited 4-2-2022
import threading, json, time, Windows, os
from infi.systray import SysTrayIcon
from pynput import mouse, keyboard
from tendo import singleton

os.chdir(os.path.dirname(os.path.abspath(__file__))) # changing the working directory to the directory where the script is

Me = singleton.SingleInstance() # To prevent multiple instances from running at the same time
Lock = threading.Lock()

class VariablesClass():
	def __init__(self):
		with open("Data.json") as File: # read the data from the file and assign variables to it
			Data = json.loads(File.read())
			self.LeftMouseClicks = Data["Left Clicks"]
			self.RightMouseClicks = Data["Right Clicks"]
			self.MiddleMouseClicks = Data["Middle Clicks"]
			self.MouseScrolls = Data["Scrolls"]
			self.KeyPresses = Data["Key Presses"]
			self.LastLeftMouseClicksValue = self.LeftMouseClicks # Need those variables so that I can throttle how many times it saves to the file
			self.LastRightMouseClicksValue = self.RightMouseClicks
			self.LastMiddleMouseClicksValue = self.MiddleMouseClicks
			self.LastMouseScrollsValue = self.MouseScrolls
			self.LastKeyPressesValue = self.KeyPresses
Variables = VariablesClass()

def Quit(systray):
	os._exit(1) # I have no idea what the heck this does but it terminates all the running threads which is what I need
# and apparently I need to have an int as an argument and idk whats the difference between each number but 1 worked so
# thats what I used.

def ShowStats(systray):
	Windows.OpenStatsWindow()

def Save():
	Lock.acquire() # using lock here becuase this function is called from two different threads which can lead to a race condition
	with open("Data.json", "w") as File: # opening and writing data in the file
		Data = {}
		Data["Left Clicks"] = Variables.LeftMouseClicks
		Data["Right Clicks"] = Variables.RightMouseClicks
		Data["Middle Clicks"] = Variables.MiddleMouseClicks
		Data["Scrolls"] = Variables.MouseScrolls
		Data["Key Presses"] = Variables.KeyPresses
		File.write(json.dumps(Data, indent=4))
	Lock.release()

def InitializeMouse():
	def OnClick(x, y, button, pressed):
		if pressed:
			if button == button.left: # check if its a left click
				Variables.LeftMouseClicks += 1
				if Variables.LeftMouseClicks - Variables.LastLeftMouseClicksValue == 5: # check if left clicks was clicked then save 
					Variables.LastLeftMouseClicksValue = Variables.LeftMouseClicks
					Save()
			if button == button.right: # check if its a right click
				Variables.RightMouseClicks += 1
				if Variables.RightMouseClicks - Variables.LastRightMouseClicksValue == 5:
					Variables.LastRightMouseClicksValue = Variables.RightMouseClicks
					Save()
			if button == button.middle: # check if its a middle click
				Variables.MiddleMouseClicks += 1
				if Variables.MiddleMouseClicks - Variables.LastMiddleMouseClicksValue == 5:
					Variables.LastMiddleMouseClicksValue = Variables.MiddleMouseClicks
					Save()

	def OnScroll(x, y, dx, dy):
		Variables.MouseScrolls += 1
		if Variables.MouseScrolls - Variables.LastMouseScrollsValue == 5: # check if its a scroll
			Variables.LastMouseScrollsValue = Variables.MouseScrolls
			Save()

	with mouse.Listener(on_click=OnClick, on_scroll=OnScroll) as listener:
		listener.join()
	
def InitializeKeyboard():

	def OnRelease(key):
		Variables.KeyPresses += 1
		if Variables.KeyPresses - Variables.LastKeyPressesValue == 5: # The reason I am only counting the released keys is because if I
			Variables.LastKeyPressesValue = Variables.KeyPresses # hold a key for a while it will register multiple key presses but you
			Save() # can only release a key once after pressing it.

	with keyboard.Listener(on_release=OnRelease) as KeyboardListener:
		KeyboardListener.join()
# Launching the system tray
menu_options = (("Show Stats", None, ShowStats),)
systray = SysTrayIcon("icon.ico", "Whatpulse Alternative", menu_options, on_quit=Quit)
systray.start()

MouseThread = threading.Thread(target=InitializeMouse, args=()) # Create a thread for the mouse
KeyboardThread = threading.Thread(target=InitializeKeyboard, args=()) # Create a thread for the keyboard
# start both threads
MouseThread.start()
KeyboardThread.start()
