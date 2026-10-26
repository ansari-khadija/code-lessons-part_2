# C. Menu and toolbar widgets
'''QMenuBar — menu bar at the top of a window.
QMenu — drop-down menu.
QAction — command used in menus and toolbars.
QToolBar — toolbar containing actions and buttons.'''


import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QToolBar, QTextEdit
)


class MenuToolbarDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu and Toolbar Widgets")
        self.setGeometry(200, 200, 600, 400)

        # Central text editor
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # 1. QMenuBar
        menubar = self.menuBar()

        # 2. QMenu
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")

        # 3. QAction
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        copy_action = QAction("Copy", self)
        copy_action.triggered.connect(self.editor.copy)

        paste_action = QAction("Paste", self)
        paste_action.triggered.connect(self.editor.paste)

        # Add actions to menus
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # 4. QToolBar
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)

        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

    def new_file(self):
        self.editor.clear()

    def open_file(self):
        self.editor.setText("Open action selected.")

    def save_file(self):
        self.editor.setText("Save action selected.")


app = QApplication(sys.argv)
window = MenuToolbarDemo()
window.show()
sys.exit(app.exec_())
