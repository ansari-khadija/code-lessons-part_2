#  Drag and Drop in PyQt5


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout
)
from PyQt5.QtCore import Qt


class DropWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drag and Drop Demo")
        self.setGeometry(300, 200, 500, 350)

        self.instruction = QLabel(
            "Drag a file or text and drop it here"
        )
        self.instruction.setAlignment(Qt.AlignCenter)

        self.result = QLabel("Waiting for a drop...")
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setWordWrap(True)

        self.result.setStyleSheet("""
            QLabel {
                border: 2px dashed #3498db;
                padding: 25px;
                background-color: #f0f8ff;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.instruction)
        layout.addWidget(self.result)
        self.setLayout(layout)

        # Allow drag-and-drop operations
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        # Accept files or text
        if (event.mimeData().hasUrls()
                or event.mimeData().hasText()):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if (event.mimeData().hasUrls()
                or event.mimeData().hasText()):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        mime = event.mimeData()

        if mime.hasUrls():
            files = [
                url.toLocalFile()
                for url in mime.urls()
                if url.isLocalFile()
            ]

            if files:
                self.result.setText(
                    "Dropped files:\n" + "\n".join(files)
                )
            else:
                self.result.setText(
                    "No local files were dropped."
                )

        elif mime.hasText():
            self.result.setText(
                "Dropped text:\n" + mime.text()
            )

        event.acceptProposedAction()


app = QApplication(sys.argv)
window = DropWindow()
window.show()
sys.exit(app.exec_())
