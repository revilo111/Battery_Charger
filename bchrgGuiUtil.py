from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSlider, QLabel, QLineEdit, QTabWidget
from PySide6.QtCore import Qt

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

def createTextInputCenter(name, size):
        input = QLineEdit()
        input.setPlaceholderText(name)
        input.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        input.setFixedWidth(size)
        return input

def createButton(name, function, size):
        button = QPushButton(name)
        button.clicked.connect(function)
        button.setFixedWidth(size)
        return button

def createSlider(parent, panel):
        slider = QSlider(Qt.Vertical, parent)
        slider.setGeometry(parent.width() * 0.925, 0, parent.width() * 0.05, parent.height() * 0.8)
        slider.setMinimum(0)
        slider.setMaximum(panel.height() * 0.5)
        slider.setValue(0)
        slider.setInvertedAppearance(True)
        slider.valueChanged.connect(lambda: movePanel(slider.value(), panel))

def createLayout1(parent):
        layout1 = QGridLayout(parent)
        layout1.addWidget(createLabelCenter(""), 0, 0, 0, 0)
        layout1.addWidget(createLabelCenter("Default Power Settings"), 1, 0, 1, 0)
        layout1.addWidget(createLabelCenter("Stop threshold % ( 0 - 100 )"), 2, 0, 2, 0)
        layout1.addWidget(createTextInputCenter("<Integer within 0 and 100>", parent.width() * 0.75), 3, 0, 2, 0)
        layout1.addWidget(createLabelCenter("Start threshold % ( 0 - 100 )"), 4, 0, 2, 0)
        layout1.addWidget(createTextInputCenter("<Integer within 0 and 100>", parent.width() * 0.75), 5, 0, 2, 0)
        layout1.addWidget(createButton("Save", tab1Function, parent.width() * 0.5), 6, 0, 4, 0, alignment=Qt.AlignCenter)

def tab1Function(null):
        print("Lol")

def movePanel(y, panel):
    panel.move(panel.x(), -y)

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
