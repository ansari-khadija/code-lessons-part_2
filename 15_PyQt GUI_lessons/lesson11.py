# E. List and scrolling widgets
'''QListWidget — displays a list of items.
QListView — displays list data using a model.
QScrollBar — horizontal or vertical scrolling control.
'''


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QListWidget, QListView, QScrollBar
)
from PyQt5.QtCore import QStringListModel, Qt


class ListScrollDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List and Scrolling Widgets")
        self.setGeometry(200, 200, 400, 450)

        layout = QVBoxLayout()

        # 1. QListWidget
        layout.addWidget(QLabel("1. QListWidget"))

        list_widget = QListWidget()
        list_widget.addItems([
            "Apple", "Banana", "Mango",
            "Orange", "Grapes"
        ])
        list_widget.currentTextChanged.connect(
            lambda text: self.status.setText(
                "Selected: " + text
            )
        )
        layout.addWidget(list_widget)

        # 2. QListView
        layout.addWidget(QLabel("2. QListView"))

        items = ["Python", "Java", "C++", "JavaScript"]

        model = QStringListModel(items)
        list_view = QListView()
        list_view.setModel(model)
        list_view.clicked.connect(
            lambda index: self.status.setText(
                "Selected: " + model.data(index)
            )
        )
        layout.addWidget(list_view)

        # 3. QScrollBar
        layout.addWidget(QLabel("3. QScrollBar"))

        scrollbar = QScrollBar(Qt.Horizontal)
        scrollbar.setRange(0, 100)
        scrollbar.setValue(25)

        self.value_label = QLabel("Scroll value: 25")
        scrollbar.valueChanged.connect(
            lambda value: self.value_label.setText(
                f"Scroll value: {value}"
            )
        )

        layout.addWidget(scrollbar)
        layout.addWidget(self.value_label)

        # Status label
        self.status = QLabel("Select an item from a list")
        layout.addWidget(self.status)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = ListScrollDemo()
window.show()
sys.exit(app.exec_())
