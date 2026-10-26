# Multiple Document Interface (MDI) in PyQt5


import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMdiArea,
    QMdiSubWindow,
    QTextEdit,
    QAction
)


class MDIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 MDI Application")
        self.setGeometry(100, 100, 900, 600)

        # MDI workspace
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # Create menu bar
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")

        new_action = QAction("New Document", self)
        new_action.triggered.connect(self.new_document)
        file_menu.addAction(new_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Window menu
        window_menu = menu_bar.addMenu("Window")

        cascade_action = QAction("Cascade", self)
        cascade_action.triggered.connect(
            self.mdi.cascadeSubWindows
        )
        window_menu.addAction(cascade_action)

        tile_action = QAction("Tile", self)
        tile_action.triggered.connect(
            self.mdi.tileSubWindows
        )
        window_menu.addAction(tile_action)

        # Open first document
        self.new_document()

    def new_document(self):
        # Create text editor
        editor = QTextEdit()
        editor.setPlainText("Write your document here...")

        # Create child window
        sub_window = QMdiSubWindow()
        sub_window.setWidget(editor)
        sub_window.setWindowTitle(
            f"Document {len(self.mdi.subWindowList()) + 1}"
        )

        # Add child window to MDI workspace
        self.mdi.addSubWindow(sub_window)
        sub_window.resize(350, 250)
        sub_window.show()


app = QApplication(sys.argv)

window = MDIWindow()
window.show()

sys.exit(app.exec_())
