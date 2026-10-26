# D. Container and layout widgets
'''QTabWidget — organizes content into tabs.
QStackedWidget — displays one widget at a time.
QSplitter — resizable areas separated by a divider.
QDockWidget — movable or dockable panel.
QGroupBox — groups related widgets.
QScrollArea — provides a scrollable area.'''


import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QTabWidget, QStackedWidget,
    QSplitter, QDockWidget, QGroupBox, QScrollArea,
    QTextEdit, QListWidget
)
from PyQt5.QtCore import Qt


class ContainerDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Container and Layout Widgets")
        self.setGeometry(100, 100, 800, 600)

        # 1. QTabWidget
        tabs = QTabWidget()

        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("Welcome to Tab 1"))
        tab1_layout.addWidget(QPushButton("Button 1"))
        tab1.setLayout(tab1_layout)

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("Welcome to Tab 2"))
        tab2_layout.addWidget(QPushButton("Button 2"))
        tab2.setLayout(tab2_layout)

        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")

        # 2. QStackedWidget
        stacked = QStackedWidget()

        page1 = QLabel("Stacked Page 1")
        page1.setAlignment(Qt.AlignCenter)

        page2 = QLabel("Stacked Page 2")
        page2.setAlignment(Qt.AlignCenter)

        stacked.addWidget(page1)
        stacked.addWidget(page2)

        switch_button = QPushButton("Switch Stacked Page")
        switch_button.clicked.connect(
            lambda: stacked.setCurrentIndex(
                1 - stacked.currentIndex()
            )
        )

        stack_layout = QVBoxLayout()
        stack_layout.addWidget(stacked)
        stack_layout.addWidget(switch_button)

        stack_page = QWidget()
        stack_page.setLayout(stack_layout)

        # 3. QSplitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(QLabel("Left Panel"))
        splitter.addWidget(QTextEdit("Right Panel"))
        splitter.setSizes([200, 400])

        # 5. QGroupBox
        group = QGroupBox("User Information")
        group_layout = QVBoxLayout()
        group_layout.addWidget(QLabel("Name: Student"))
        group_layout.addWidget(QLabel("Course: Python"))
        group.setLayout(group_layout)

        # 6. QScrollArea
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout()

        for i in range(1, 21):
            scroll_layout.addWidget(
                QLabel(f"Scrollable Item {i}")
            )

        scroll_content.setLayout(scroll_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)

        # Main tab layout
        main_tabs = QTabWidget()
        main_tabs.addTab(tabs, "QTabWidget")
        main_tabs.addTab(stack_page, "QStackedWidget")
        main_tabs.addTab(splitter, "QSplitter")
        main_tabs.addTab(group, "QGroupBox")
        main_tabs.addTab(scroll_area, "QScrollArea")

        self.setCentralWidget(main_tabs)

        # 4. QDockWidget
        dock = QDockWidget("Dockable Panel", self)
        dock.setWidget(QListWidget())
        dock.widget().addItems(
            ["Item 1", "Item 2", "Item 3"]
        )
        self.addDockWidget(Qt.RightDockWidgetArea, dock)


app = QApplication(sys.argv)
window = ContainerDemo()
window.show()
sys.exit(app.exec_())
