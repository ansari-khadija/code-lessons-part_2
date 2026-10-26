# QVBoxLayout Example
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QVBoxLayout")
window.resize(300, 250)

btn1 = QPushButton("Button 1")
btn2 = QPushButton("Button 2")
btn3 = QPushButton("Button 3")

layout = QVBoxLayout()

layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
