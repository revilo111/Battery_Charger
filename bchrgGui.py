
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QPushButton, QLabel, QGridLayout, QLineEdit, QSlider
from PySide6.QtCore import QSize, Qt
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Battery_Charge")
screen = window.screen().availableGeometry()
window.setFixedSize(screen.width() // 5, screen.height() // 2.5)

def centerWindow(window):
	fg = window.frameGeometry()
	fg.moveCenter(window.screen().availableGeometry().center())
	window.move(fg.topLeft())

def setTabs(window, tab1, tab2):
	tabs = QTabWidget()
	window.setCentralWidget(tabs)
	tabs.addTab(tab1, "Default")
	tabs.addTab(tab2, "Charge Options")
	tabBar = tabs.tabBar()
	tabs.setStyleSheet("QTabBar::tab { width: " + str(window.width() // 2) + "px; height: " + str(window.height() // 10) + "px }")

def createLabelCenter(name):
	label = QLabel(name)
	label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
	label.setFocusPolicy(Qt.StrongFocus)
	return label

def createTextInputCenter(name, size=window.width() * 0.75):
	input = QLineEdit()
	input.setPlaceholderText(name)
	input.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
	input.setFixedWidth(size)
	return input

def createButton(name, function, size=window.width() * 0.5):
	button = QPushButton(name)
	button.clicked.connect(function)
	button.setFixedWidth(size)
	return button

def createSlider(parent, panel):
	slider = QSlider(Qt.Vertical, parent)
	slider.setGeometry(tab2.width() * 0.925, 0, tab2.width() * 0.05, tab2.height() * 0.8)
	slider.setMinimum(0)
	slider.setMaximum(panel.height() * 0.5)
	slider.setValue(0)
	slider.setInvertedAppearance(True)
	slider.valueChanged.connect(movePanel)

def createLayout1(parent):
	layout1 = QGridLayout(parent)
	layout1.addWidget(createLabelCenter(""), 0, 0, 0, 0)
	layout1.addWidget(createLabelCenter("Default Power Settings"), 1, 0, 1, 0)
	layout1.addWidget(createLabelCenter("Stop threshold % ( 0 - 100 )"), 2, 0, 2, 0)
	layout1.addWidget(createTextInputCenter("<Integer within 0 and 100>"), 3, 0, 2, 0)
	layout1.addWidget(createLabelCenter("Start threshold % ( 0 - 100 )"), 4, 0, 2, 0)
	layout1.addWidget(createTextInputCenter("<Integer within 0 and 100>"), 5, 0, 2, 0)
	layout1.addWidget(createButton("Save", tab1Function), 6, 0, 4, 0, alignment=Qt.AlignCenter)

def tab1Function(null):
	print("Lol")

def movePanel(y):
    panel.move(panel.x(), -y)

centerWindow(window)

tab1 = QWidget()

createLayout1(tab1)

tab2 = QWidget()
tab2.setFixedSize(window.width(), window.height() * 0.9)


"""
panel = QWidget(tab2)
panel.setFocusPolicy(Qt.StrongFocus)
panel.setFixedSize(tab2.width() * 0.9, tab2.height() * 2)

createSlider(tab2, panel)

def deleteEntry(index):
	print(index)
	entry = panelLayout.itemAtPosition(index, 0).widget()
	panelLayout.removeWidget(entry)
	entry.deleteLater()
	if(panelLayout.count() == 9):
		panelLayout.itemAtPosition(9, 0).widget().setVisible(True)
	for row in range(index + 1, panelLayout.count()):
		print(index, row)
		item = panelLayout.itemAtPosition(row, 0).widget()
		panelLayout.removeWidget(item)
		panelLayout.addWidget(item, row - 1, 0)

		exitButton = panelLayout.itemAtPosition(row - 1, 0).widget().findChild(QPushButton, "exit")
		exitButton.clicked.disconnect()
		exitButton.clicked.connect(lambda: deleteEntry(index + row))

		for child in panelLayout.itemAtPosition(row - 1, 0).widget().children():
			print(child)


class EntryFrame(QWidget):
    def __init__(self, panel, delete_callback):
        super().__init__(panel)

        self.panel = panel
        self.delete_callback = delete_callback

        self.setObjectName("entry")
        self.setStyleSheet("#entry { border: 1px solid darkgray; border-radius: 2px; }")

        self.setFixedSize(panel.width() * 0.95, panel.height() * 0.095)

        layout = QGridLayout(self)

        layout.addWidget(createLabelCenter("Start %"), 0, 0)
        layout.addWidget(createTextInputCenter("<0-100>", panel.width() // 4), 1, 0)

        layout.addWidget(createLabelCenter("Stop %"), 0, 1)
        layout.addWidget(createTextInputCenter("<0-100>", panel.width() // 4), 1, 1)

        layout.addWidget(createLabelCenter("Start time"), 0, 2)
        layout.addWidget(createTextInputCenter("<hh:mm>", panel.width() // 4), 1, 2)

        # Exit button
        self.exitButton = createButton("x", self.on_delete, self.width() // 25, panel.entries.count)
        self.exitButton.setParent(self)
        self.exitButton.setObjectName("exit")
        self.exitButton.setGeometry(
            self.width() * 0.95,
            self.height() * 0.05,
            self.width() * 0.05,
            self.height() * 0.2
        )

    def on_delete(self, null):
        self.delete_callback(self)

class Panel(QWidget):
    def __init__(self, tab):
        super().__init__(tab)

        self.layout = QGridLayout(self)
        self.entries = []

    def add_entry(self):
        entry = EntryWidget(self, self.delete_entry)

        row = len(self.entries)
        self.entries.append(entry)

        self.layout.addWidget(entry, row, 0)

        # Hide 10th row if needed
        if len(self.entries) == 10:
            entry.setVisible(False)

    def delete_entry(self, entry):
        if entry in self.entries:
            row = self.entries.index(entry)

            self.layout.removeWidget(entry)
            entry.deleteLater()
            self.entries.remove(entry)

            # Re-pack remaining entries
            for i, e in enumerate(self.entries):
                self.layout.addWidget(e, i, 0)

"""

class Profile(QWidget):
	def __init__(self, panel, deleteCallback):
		super().__init__(panel)

		self.panel = panel
		self.deleteCallback = deleteCallback

		self.setFixedSize(panel.width() * 0.95, panel.height() * 0.095)

		layout = QGridLayout(self)

		layout.addWidget(createLabelCenter("Start %"), 0, 0)
		layout.addWidget(createTextInputCenter("<0-100>", panel.width() // 4), 1, 0)

		layout.addWidget(createLabelCenter("Stop %"), 0, 1)
		layout.addWidget(createTextInputCenter("<0-100>", panel.width() // 4), 1, 1)

		layout.addWidget(createLabelCenter("Start time"), 0, 2)
		layout.addWidget(createTextInputCenter("<hh:mm>", panel.width() // 4), 1, 2)

		self.exitButton = createButton("x", self.onDelete, self.width() // 25)
		self.exitButton.setParent(self)
		self.exitButton.setGeometry(self.width() * 0.95, self.height() * 0.05, self.width() * 0.05, self.height() * 0.2)

	def onDelete(self):
		self.deleteCallback(self)

class Panel(QWidget):
	def __init__(self, tab):
		super().__init__(tab)

		self.layout = QGridLayout(self)
		self.profiles = []
		self.addProfileButton = createButton("+", self.addProfile, tab.width() * 0.09)

		self.layout.addWidget(self.addProfileButton, 9, 0, alignment=Qt.AlignCenter)
		self.layout.setRowStretch(10, 1)

	def addProfile(self):
		profile = Profile(self, self.deleteProfile)

		row = len(self.profiles)
		self.profiles.append(profile)
		self.layout.addWidget(profile, row, 0)

		if(len(self.profiles) == 9):
			self.addProfileButton.setVisible(False)

	def deleteProfile(self, profile):
		if profile in self.profiles:
			row = self.profiles.index(profile)

			self.layout.removeWidget(profile)
			profile.deleteLater()
			self.profiles.remove(profile)

			for i, p in enumerate(self.profiles):
				self.layout.addWidget(p, i, 0)

			self.addProfileButton.setVisible(True)

panel = Panel(tab2)
panel.setFocusPolicy(Qt.StrongFocus)
panel.setFixedSize(tab2.width() * 0.9, tab2.height() * 2)
createSlider(tab2, panel)
"""
panel.add_entry()
panel.add_entry()
"""
"""
def addBlankEntry(null):
	entry = QWidget()
	entry.setFixedSize(panel.width() * 0.95, panel.height() * 0.095)
	entryLayout = QGridLayout(entry)
	entryLayout.addWidget(createLabelCenter("Start %"), 0, 0, 1, 1)
	entryLayout.addWidget(createTextInputCenter("<0-100>", panel.width() // 4), 1, 0, 1, 1)
	entryLayout.addWidget(createLabelCenter("Stop %"), 0, 1, 1, 1)
	entryLayout.addWidget(createTextInputCenter("<0-100>", panel.width() // 4), 1, 1, 1, 1)
	entryLayout.addWidget(createLabelCenter("Start time"), 0, 2, 1, 1)
	entryLayout.addWidget(createTextInputCenter("<hh:mm>", panel.width() // 4), 1, 2, 1, 1)

	exitButton = createButton("x", deleteEntry, entry.width() // 25, panelLayout.count() - 1)
	exitButton.setParent(entry)
	exitButton.setObjectName("exit")
	exitButton.setGeometry(entry.width() * 0.95, entry.height() * 0.05, entry.width() * 0.05, entry.height() * 0.2)

	entry.setObjectName("entry")
	entry.setStyleSheet("#entry { border: 1px solid dark-gray; border-radius: 2px; }")

	panelLayout.addWidget(entry, panelLayout.count() - 1, 0)

	if(panelLayout.count() == 10):
		panelLayout.itemAtPosition(9, 0).widget().setVisible(False)

"""



"""
panelLayout = QGridLayout(panel)
panelLayout.addWidget(createButton("+", addBlankEntry, panel.width() // 10), 9, 0, alignment=Qt.AlignCenter)
panelLayout.setRowStretch(panelLayout.rowCount(), 1)
"""
setTabs(window, tab1, tab2)
window.show()
app.exec()

