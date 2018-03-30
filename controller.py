__version__ = "0.0.1"

import sys
sys.path.insert(0, "C:/Users/Kade/Desktop/School/Programming/Python/modules")

import GUI_Maker

if (__name__ == "__main__"):
	isMain = True
else:
	isMain = False

class GUI_Builder():
	def __init__(self):
		self.gui = GUI_Maker.build()

	@GUI_Maker.wrap_showError(makeDialog = not isMain)
	def buildGUI(self):
		self.createWindows()
		self.buildMainWindow()

	def createWindows(self):
		"""Creates all the window frames before they are built.
		This is because frames that would have been created first may need to address frames that would have been created after.

		Example Input: createWindows()
		"""

		self.frame_0  = self.gui.addWindow(label = 0,  title = f"Label Printer v.{__version__}")

	def buildMainWindow(self):
		"""Creates the main window.

		Example Input: buildMainWindow()
		"""

		with self.frame_0 as myFrame:
			#Initialize GUI
			myFrame.setMinimumFrameSize(size = (500, 300))
			myFrame.setWindowSize(800, 700)
			myFrame.addStatusBar()
			# myFrame.setStatusText(self.defaultStatus)

			#Build menu bar
			with myFrame.addMenu(text = "&File") as myMenu:
				with myMenu.addMenuItem(text = "Exit") as myMenuItem:
					myMenuItem.addToolTip("Closes the software")
					myMenuItem.setFunction_click(myFunction = "self.onExit")

				# myMenu.addMenuSeparator()
				
				# with myMenu.addMenuItem(text = "]Save", label = "menuUpdateLocalDatabase") as myMenuItem:
				# 	myMenuItem.addToolTip("Load the database from a remote computer to this computer")
				# 	myMenuItem.setFunction_click(myFunction = self.onSave)

			with myFrame.addMenu(text = "&Security") as myMenu:
				with myMenu.addMenuItem(text = "Login", label = "menuLogin") as myMenuItem:
					myMenuItem.addToolTip("Allows the user to edit things and enables locked options")
					# myMenuItem.setFunction_click(myFunction = self.onLogin)
				
				with myMenu.addMenuItem(text = "Logout", label = "menuLogout") as myMenuItem:
					myMenuItem.addToolTip("Keeps the user from editing things and disables some options")
					# myMenuItem.setFunction_click(myFunction = self.onLogout)
				
				myMenu.addMenuSeparator()
				
				with myMenu.addMenuItem(text = "Password Permissions", label = "menuPasswordPermissions") as myMenuItem:
					myMenuItem.addToolTip("View and change what permissions different users have")
					# myMenuItem.setFunction_click(myFunction = self.frame_21.onShowWindow)
				
				with myMenu.addMenuItem(text = "Generate Temporary Password", label = "menuPasswordTemp") as myMenuItem:
					myMenuItem.addToolTip("Generate temporary passwords that can be used on different computers")
					# myMenuItem.setFunction_click(myFunction = self.frame_22.onShowWindow)

			with myFrame.addMenu(text = "&Settings") as myMenu:
				with myMenu.addMenuItem(text = "User Settings", label = "menuUserSettings") as myMenuItem:
					myMenuItem.addToolTip("View and change various parameters for how this software operates")
					# myMenuItem.setFunction_click(myFunction = self.frame_16.onShowWindow)
				
				myMenu.addMenuSeparator()
				
				with myMenu.addMenuItem(text = "Change Password", label = "menuChangePassword") as myMenuItem:
					myMenuItem.addToolTip("Change the password to edit and unlock certain options")
					# myMenuItem.setFunction_click(myFunction = self.onChangePassword)

			# with myFrame.addMenu(text = "&Utilities") as myMenu:			
			# 	with myMenu.addMenuItem(text = "Debugging", label = "menuDebugging", check = True, default = self.debugging, enabled = self.enableDebugging) as myMenuItem:
			# 		myMenuItem.addToolTip("If debugging information should be printed to the cmd window and/or written in the cmd log")
			# 		myMenuItem.setFunction_click(myFunction = self.onSetDebugging)

			#Setup for content
			with myFrame.addSizerGridFlex(rows = 1, columns = 1) as mainSizer:
				mainSizer.growFlexColumnAll()
				mainSizer.growFlexRowAll()

				mainSizer.addText("Lorem")

class Controller(GUI_Builder):
	def __init__(self):
		#Initialize inherited modules
		GUI_Builder.__init__(self)

	def begin(self):
		self.buildGUI()
		# self.gui.centerWindowAll()

		self.frame_0.showWindow()

		if __name__ == '__main__':
			print("GUI Finished Bulding")

		self.gui.finish()

#Run Program
if __name__ == '__main__':
	controller = Controller()
	controller.begin()