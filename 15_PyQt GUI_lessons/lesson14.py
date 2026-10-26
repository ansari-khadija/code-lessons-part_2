# QMessageBox types example
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QMessageBox, QVBoxLayout
)


class MessageDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox Demo")
        self.setGeometry(300, 200, 350, 250)

        info_btn = QPushButton("Information")
        warning_btn = QPushButton("Warning")
        error_btn = QPushButton("Critical Error")
        question_btn = QPushButton("Ask Question")

        layout = QVBoxLayout()
        layout.addWidget(info_btn)
        layout.addWidget(warning_btn)
        layout.addWidget(error_btn)
        layout.addWidget(question_btn)
        self.setLayout(layout)

        info_btn.clicked.connect(self.show_info)
        warning_btn.clicked.connect(self.show_warning)
        error_btn.clicked.connect(self.show_error)
        question_btn.clicked.connect(self.ask_question)

    def show_info(self):
        QMessageBox.information(
            self, "Information",
            "Welcome to PyQt5!"
        )

    def show_warning(self):
        QMessageBox.warning(
            self, "Warning",
            "Please check your input."
        )

    def show_error(self):
        QMessageBox.critical(
            self, "Error",
            "Something went wrong!"
        )

    def ask_question(self):
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Do you want to continue?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            QMessageBox.information(
                self, "Result", "You selected Yes."
            )
        else:
            QMessageBox.information(
                self, "Result", "You selected No."
            )


app = QApplication(sys.argv)
window = MessageDemo()
window.show()
sys.exit(app.exec_())
