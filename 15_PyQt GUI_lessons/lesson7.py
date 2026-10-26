# A. Basic Display and Input Widgets in PyQt5
'''QLabel — displays text.

QLineEdit — accepts single-line text.

QInputDialog — asks the user for input.

QFontDialog — lets the user choose a font.

QFileDialog — opens a file.
'''

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QInputDialog, QFontDialog,
    QFileDialog, QVBoxLayout
)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Category A - Basic Widgets")
        self.setGeometry(300, 100, 400, 350)

        # Layout
        layout = QVBoxLayout()

        # 1. QLabel
        self.label = QLabel("Welcome to PyQt5")
        layout.addWidget(self.label)

        # 2. QLineEdit
        self.line = QLineEdit()
        self.line.setPlaceholderText("Enter your name")
        layout.addWidget(self.line)

        # Button to display text
        btn1 = QPushButton("Show Name")
        btn1.clicked.connect(self.show_name)
        layout.addWidget(btn1)

        # 3. QInputDialog
        btn2 = QPushButton("Input Dialog")
        btn2.clicked.connect(self.input_dialog)
        layout.addWidget(btn2)

        # 4. QFontDialog
        btn3 = QPushButton("Choose Font")
        btn3.clicked.connect(self.choose_font)
        layout.addWidget(btn3)

        # 5. QFileDialog
        btn4 = QPushButton("Open File")
        btn4.clicked.connect(self.open_file)
        layout.addWidget(btn4)

        self.setLayout(layout)

    # Display text from QLineEdit
    def show_name(self):
        name = self.line.text()
        self.label.setText("Hello, " + name)

    # Input Dialog
    def input_dialog(self):
        text, ok = QInputDialog.getText(
            self, "Input Dialog", "Enter your city:"
        )
        if ok:
            self.label.setText("City: " + text)

    # Font Dialog
    def choose_font(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.label.setFont(font)

    # File Dialog
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*);;Text Files (*.txt)"
        )
        if filename:
            self.label.setText("File: " + filename)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
