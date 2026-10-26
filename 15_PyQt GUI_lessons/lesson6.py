# QStacked Layout Example


import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QStackedLayout
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QStackedLayout")
window.resize(350, 250)

# Create pages
page1 = QWidget()
page2 = QWidget()

# Page 1 content
label1 = QLabel("This is Page 1")
button1 = QPushButton("Go to Page 2")

layout1 = QVBoxLayout()
layout1.addWidget(label1)
layout1.addWidget(button1)
page1.setLayout(layout1)

# Page 2 content
label2 = QLabel("This is Page 2")
button2 = QPushButton("Go to Page 1")

layout2 = QVBoxLayout()
layout2.addWidget(label2)
layout2.addWidget(button2)
page2.setLayout(layout2)

# Create stacked layout
stack = QStackedLayout()
stack.addWidget(page1)
stack.addWidget(page2)

# Switch pages
button1.clicked.connect(lambda: stack.setCurrentIndex(1))
button2.clicked.connect(lambda: stack.setCurrentIndex(0))

window.setLayout(stack)

window.show()
sys.exit(app.exec())
