# Clipboard in PyQt5


import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)


class ClipboardDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Clipboard Demo")
        self.setGeometry(300, 200, 500, 350)

        # Multiline text editor
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText(
            "Type your text here..."
        )

        # Buttons
        copy_btn = QPushButton("Copy")
        paste_btn = QPushButton("Paste")
        clear_btn = QPushButton("Clear")

        # Horizontal button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(copy_btn)
        button_layout.addWidget(paste_btn)
        button_layout.addWidget(clear_btn)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Button events
        copy_btn.clicked.connect(self.copy_text)
        paste_btn.clicked.connect(self.paste_text)
        clear_btn.clicked.connect(self.clear_text)

    def copy_text(self):
        text = self.text_area.textCursor().selectedText()

        if not text:
            text = self.text_area.toPlainText()

        if text:
            QApplication.clipboard().setText(text)
            QMessageBox.information(
                self, "Copied", "Text copied successfully!"
            )
        else:
            QMessageBox.warning(
                self, "Warning", "There is no text to copy."
            )

    def paste_text(self):
        text = QApplication.clipboard().text()

        if text:
            self.text_area.insertPlainText(text)
        else:
            QMessageBox.warning(
                self, "Warning", "Clipboard is empty."
            )

    def clear_text(self):
        self.text_area.clear()


app = QApplication(sys.argv)
window = ClipboardDemo()
window.show()
sys.exit(app.exec_())

