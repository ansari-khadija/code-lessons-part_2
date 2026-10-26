# QGRid Layout Example


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QGridLayout")
window.resize(350, 250)

btn1 = QPushButton("Button 1")
btn2 = QPushButton("Button 2")
btn3 = QPushButton("Button 3")
btn4 = QPushButton("Button 4")

layout = QGridLayout()

layout.addWidget(btn1, 0, 0)
layout.addWidget(btn2, 0, 1)
layout.addWidget(btn3, 1, 0)
layout.addWidget(btn4, 1, 1)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
