# QH BoxLayout Example


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QHBoxLayout")
window.resize(400, 150)

btn1 = QPushButton("Button 1")
btn2 = QPushButton("Button 2")
btn3 = QPushButton("Button 3")

layout = QHBoxLayout()

layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
