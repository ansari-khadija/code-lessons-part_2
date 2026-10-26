# G. Main window and status widgets
'''QMainWindow — main application window.

QStatusBar — displays status messages at the bottom.

QProgressBar — shows task progress. start with A'''


import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QPushButton, QProgressBar,
    QLabel
)
from PyQt5.QtCore import QTimer


class MainWindowDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. QMainWindow
        self.setWindowTitle("Main Window and Status Widgets")
        self.setGeometry(200, 200, 400, 250)

        # Central widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Welcome to PyQt5")
        layout.addWidget(label)

        # 3. QProgressBar
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        # Start button
        self.button = QPushButton("Start Progress")
        self.button.clicked.connect(self.start_progress)
        layout.addWidget(self.button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 2. QStatusBar
        self.statusBar().showMessage("Ready")

        # Timer for progress
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

    def start_progress(self):
        self.progress.setValue(0)
        self.statusBar().showMessage("Progress started...")
        self.button.setEnabled(False)
        self.timer.start(100)

    def update_progress(self):
        value = self.progress.value() + 2
        self.progress.setValue(value)

        if value >= 100:
            self.timer.stop()
            self.statusBar().showMessage("Task completed!")
            self.button.setEnabled(True)


app = QApplication(sys.argv)
window = MainWindowDemo()
window.show()
sys.exit(app.exec_())
