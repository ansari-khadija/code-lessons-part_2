# modules and tools

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My First PyQt GUI")
window.resize(400, 250)

label = QLabel("Welcome to PyQt!")
button = QPushButton("Click Me")

button.clicked.connect(
    lambda: label.setText("Button clicked!")
)

layout = QVBoxLayout()
layout.addWidget(label)  # Align center
layout.addWidget(button)  # Align center

window.setLayout(layout)
window.show()

sys.exit(app.exec())