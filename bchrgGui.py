
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QPushButton, QLabel, QGridLayout, QLineEdit, QSlider
from PySide6.QtCore import QSize, Qt
import sys
import bchrgGuiUtil as util

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Battery_Charge")
screen = window.screen().availableGeometry()
window.setFixedSize(screen.width() // 5, screen.height() // 2.5)

util.centerWindow(window)

tab1 = QWidget()
tab1.setFixedSize(window.width(), window.height() * 0.9)
util.createLayout1(tab1)

tab2 = QWidget()
tab2.setFixedSize(window.width(), window.height() * 0.9)

panel = util.Panel(tab2)
panel.setFocusPolicy(Qt.StrongFocus)
panel.setFixedSize(tab2.width() * 0.9, tab2.height() * 2)

util.createSlider(tab2, panel)

util.setTabs(window, tab1, tab2)
window.show()
app.exec()

