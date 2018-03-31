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
		"""The GUI build routine.

		Example Input: buildGUI()
		"""

		self.createWindows()
		
		self.buildMainWindow()
		self.buildEditCards()
		self.buildEditFormats()
		self.buildViewCards()
		self.buildPractice()

	def createWindows(self):
		"""Creates all the window frames before they are built.
		This is because frames that would have been created first may need to address frames that would have been created after.

		Example Input: createWindows()
		"""

		self.frame_mainMenu     = self.gui.addWindow(label = "mainMenu",    title = f"Main Menu v.{__version__}")
		self.frame_editCards    = self.gui.addWindow(label = "editCards",   title = f"Edit Cards v.{__version__}")
		self.frame_editFormats  = self.gui.addWindow(label = "editFormats", title = f"Edit Formats v.{__version__}")
		self.frame_viewCards    = self.gui.addWindow(label = "viewCards",   title = f"View Cards v.{__version__}")
		self.frame_practice     = self.gui.addWindow(label = "practice",    title = f"Practice! v.{__version__}")
		# self.frame_flashCard    = self.gui.addWindow(label = "flashCard",   title = f"Flash Card v.{__version__}")

	def addCommonMenu(self, myFrame):
		"""Makes a common menu for all frames.

		Example Input: addCommonMenu(self.frame_mainMenu)
		"""
		with myFrame.addMenu(text = "&File") as myMenu:
			with myMenu.addMenuItem(text = "Exit") as myMenuItem:
				myMenuItem.addToolTip("Closes the software")
				myMenuItem.setFunction_click(myFunction = myFrame.onExit)
			
			with myMenu.addMenuItem(text = "Save", label = "menuUpdateLocalDatabase") as myMenuItem:
				myMenuItem.addToolTip("Save changes made to local database")
			# 	myMenuItem.setFunction_click(myFunction = self.onSave)

			myMenu.addMenuSeparator()

			if (myFrame != self.frame_mainMenu):
				with myMenu.addMenuItem(text = "Main Menu") as myMenuItem:
					myMenuItem.addToolTip("Returns to the main menu")
					myMenuItem.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_mainMenu)

			if (myFrame != self.frame_editCards):
				with myMenu.addMenuItem(text = "Edit Cards") as myMenuItem:
					myMenuItem.addToolTip("Switches to the card edit window")
					myMenuItem.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_editCards)

			if (myFrame != self.frame_editFormats):
				with myMenu.addMenuItem(text = "Edit Formats") as myMenuItem:
					myMenuItem.addToolTip("Switches to the format edit window")
					myMenuItem.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_editFormats)

			if (myFrame != self.frame_practice):
				with myMenu.addMenuItem(text = "Practice!") as myMenuItem:
					myMenuItem.addToolTip("Switches to the practice window")
					myMenuItem.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_practice)

		with myFrame.addMenu(text = "&Security") as myMenu:
			with myMenu.addMenuItem(text = "Login", label = "menuLogin") as myMenuItem:
				myMenuItem.addToolTip("Allows the user to edit things and enables locked options")
				# myMenuItem.setFunction_click(myFunction = self.onLogin)
			
			with myMenu.addMenuItem(text = "Logout", label = "menuLogout") as myMenuItem:
				myMenuItem.addToolTip("Keeps the user from editing things and disables some options")
				# myMenuItem.setFunction_click(myFunction = self.onLogout)

		with myFrame.addMenu(text = "&Settings") as myMenu:
			with myMenu.addMenuItem(text = "User Settings", label = "menuUserSettings") as myMenuItem:
				myMenuItem.addToolTip("View and change various parameters for how this software operates")
				# myMenuItem.setFunction_click(myFunction = self.frame_16.onShowWindow)

		# with myFrame.addMenu(text = "&Utilities") as myMenu:			
		# 	with myMenu.addMenuItem(text = "Debugging", label = "menuDebugging", check = True, default = self.debugging, enabled = self.enableDebugging) as myMenuItem:
		# 		myMenuItem.addToolTip("If debugging information should be printed to the cmd window and/or written in the cmd log")
		# 		myMenuItem.setFunction_click(myFunction = self.onSetDebugging)

	def buildMainWindow(self):
		"""Creates the main window.

		Example Input: buildMainWindow()
		"""

		with self.frame_mainMenu as myFrame:
			#Initialize GUI
			myFrame.setMinimumFrameSize(size = (200, 200))
			myFrame.addStatusBar()
			# myFrame.setStatusText(self.defaultStatus)

			#Build menu bar
			self.addCommonMenu(myFrame)

			#Setup for content
			with myFrame.addSizerGridFlex(rows = 4, columns = 1) as mainSizer:
				mainSizer.growFlexColumnAll()
				mainSizer.growFlexRowAll()

				with mainSizer.addButton("Edit Cards") as myWidget:
					myWidget.addToolTip("Edit, add, and remove cards")
					myWidget.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_editCards)

				with mainSizer.addButton("Edit Formats") as myWidget:
					myWidget.addToolTip("Edit, add, and remove formats")
					myWidget.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_editFormats)

				with mainSizer.addButton("View Cards") as myWidget:
					myWidget.addToolTip("View all cards in this deck")
					myWidget.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_editCards)

				with mainSizer.addButton("Practice!") as myWidget:
					myWidget.addToolTip("Use the created flash cards")
					myWidget.setFunction_click(myFunction = myFrame.onSwitchWindow, myFunctionArgs = self.frame_practice)

	def buildEditCards(self):
		"""Edit, add, and remove cards from here.

		Example Input: buildEditCards()
		"""

		with self.frame_editCards as myFrame:
			#Initialize GUI
			myFrame.setMinimumFrameSize(size = (200, 200))
			myFrame.addStatusBar()
			# myFrame.setStatusText(self.defaultStatus)

			#Build menu bar
			self.addCommonMenu(myFrame)

			#Setup for content
			with myFrame.addSizerGridFlex(rows = 3, columns = 1) as mainSizer:
				mainSizer.growFlexColumnAll()
				mainSizer.growFlexRowAll()

				leftSizer, rightSizer = mainSizer.addSplitterDouble(minimumSize = 20, vertical = True, dividerPosition = 130, dividerGravity = 0, panel_0 = {"border": "raised"}, panel_1 = {"border": "raised"})

				with leftSizer as mySizer:
					mySizer.addText("List all cards here")

				with rightSizer as mySizer:
					with mySizer.addTable(label = "cardTable", rows = 10, columns = 10, editOnEnter = True) as cardTable: 
						pass

				mainSizer.addButton("Show Selected Card")

	def buildEditFormats(self):
		"""Edit, add, and remove cards from here.

		Example Input: buildEditFormats()
		"""

		with self.frame_editFormats as myFrame:
			#Initialize GUI
			myFrame.setMinimumFrameSize(size = (200, 200))
			myFrame.addStatusBar()
			# myFrame.setStatusText(self.defaultStatus)

			#Build menu bar
			self.addCommonMenu(myFrame)

			#Setup for content
			with myFrame.addSizerGridFlex(rows = 3, columns = 1) as mainSizer:
				mainSizer.growFlexColumnAll()
				mainSizer.growFlexRowAll()

				mainSizer.addListTree(choices = {"Lorem": [{"Ipsum": "Dolor"}, "Sit"], "Amet": None})

				# leftSizer, rightSizer = mainSizer.addSplitterDouble(minimumSize = 20, vertical = True, dividerPosition = 130, dividerGravity = 0, panel_0 = {"border": "raised"}, panel_1 = {"border": "raised"})

				# with leftSizer as mySizer:
				# 	mySizer.addListFull()#["Lorem", "Ipsum", "Dolor", "Sit", "Amet"])

				# with rightSizer as mySizer:
				# 	leftSubSizer, rightSubSizer = mySizer.addSplitterDouble(minimumSize = 20, vertical = True, dividerPosition = 130, dividerGravity = 0, panel_0 = {"border": "raised"}, panel_1 = {"border": "raised"})

				# 	with leftSubSizer as mySubSizer:
				# 		topSubSubSizer, bottomSubSubSizer = mySizer.addSplitterDouble(minimumSize = 20, vertical = False, dividerPosition = 130, dividerGravity = 0, panel_0 = {"border": "raised"}, panel_1 = {"border": "raised"})
						
				# 		with topSubSubSizer as mySubSubSizer:
				# 			mySubSubSizer.addListFull(["Container - Grid", "Container - Flex", "Text", "Image"])

				# 		with bottomSubSubSizer as mySubSubSizer:
				# 			mySubSubSizer.addText("Edit selected item attributes here")

				# 	with rightSubSizer as mySubSizer:
				# 		mySubSizer.addListTree()

				mainSizer.addButton("Preview Selected Format")

	def buildViewCards(self):
		"""View the flash cards.

		Example Input: buildViewCards()
		"""

		with self.frame_viewCards as myFrame:
			#Initialize GUI
			myFrame.setMinimumFrameSize(size = (200, 200))
			myFrame.addStatusBar()
			# myFrame.setStatusText(self.defaultStatus)

			#Build menu bar
			self.addCommonMenu(myFrame)

			#Setup for content
			with myFrame.addSizerGridFlex(rows = 3, columns = 1) as mainSizer:
				mainSizer.growFlexColumnAll()
				mainSizer.growFlexRowAll()

				mainSizer.addText("List all cards here")

	def buildPractice(self):
		"""Use the flash cards.

		Example Input: buildPractice()
		"""

		with self.frame_practice as myFrame:
			#Initialize GUI
			myFrame.setMinimumFrameSize(size = (200, 200))
			myFrame.addStatusBar()
			# myFrame.setStatusText(self.defaultStatus)

			#Build menu bar
			self.addCommonMenu(myFrame)

			#Setup for content
			with myFrame.addSizerGridFlex(rows = 3, columns = 1) as mainSizer:
				mainSizer.growFlexColumnAll()
				mainSizer.growFlexRowAll()

				mainSizer.addButton("Set Rules")
				mainSizer.addButton("Show Card")

class Controller(GUI_Builder):
	def __init__(self):
		#Initialize inherited modules
		GUI_Builder.__init__(self)

	def begin(self):
		self.buildGUI()
		# self.gui.centerWindowAll()

		self.frame_mainMenu.showWindow()

		if __name__ == '__main__':
			print("GUI Finished Bulding")

		self.gui.finish()

#Run Program
if __name__ == '__main__':
	controller = Controller()
	controller.begin()