# QForm Layout Example


import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QFormLayout
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QFormLayout")
window.resize(350, 200)

name_label = QLabel("Name:")
name_input = QLineEdit()

email_label = QLabel("Email:")
email_input = QLineEdit()

password_label = QLabel("Password:")
password_input = QLineEdit()
password_input.setEchoMode(QLineEdit.EchoMode.Password)

btn = QPushButton("Submit")

layout = QFormLayout()

layout.addRow(name_label, name_input)
layout.addRow(email_label, email_input)
layout.addRow(password_label, password_input)
layout.addRow(btn)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
