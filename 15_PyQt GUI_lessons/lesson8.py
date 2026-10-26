# B. Buttons and selection widgets
'''QPushButton — clickable button.
QRadioButton — selects one option from a group.
QCheckBox — selects or deselects an option.
QComboBox — drop-down list.
QSpinBox — selects an integer value.
QSlider — selects a value by sliding.
QToolButton — compact button, often used on toolbars.'''


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QRadioButton, QCheckBox,
    QComboBox, QSpinBox, QSlider, QToolButton
)
from PyQt5.QtCore import Qt


class WidgetDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buttons and Selection Widgets")
        self.setGeometry(200, 200, 350, 400)

        layout = QVBoxLayout()

        # QLabel
        self.label = QLabel("Select an option")
        layout.addWidget(self.label)

        # 1. QPushButton
        button = QPushButton("Click Me")
        button.clicked.connect(
            lambda: self.label.setText("Button Clicked!")
        )
        layout.addWidget(button)

        # 2. QRadioButton
        radio = QRadioButton("Python")
        radio.toggled.connect(
            lambda checked: self.label.setText("Python selected")
            if checked else None
        )
        layout.addWidget(radio)

        # 3. QCheckBox
        checkbox = QCheckBox("I agree")
        checkbox.stateChanged.connect(
            lambda state: self.label.setText(
                "Checked" if state else "Unchecked"
            )
        )
        layout.addWidget(checkbox)

        # 4. QComboBox
        combo = QComboBox()
        combo.addItems(["Red", "Green", "Blue"])
        combo.currentTextChanged.connect(
            lambda text: self.label.setText("Color: " + text)
        )
        layout.addWidget(combo)

        # 5. QSpinBox
        spinbox = QSpinBox()
        spinbox.setRange(0, 100)
        spinbox.valueChanged.connect(
            lambda value: self.label.setText(f"Value: {value}")
        )
        layout.addWidget(spinbox)

        # 6. QSlider
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.valueChanged.connect(
            lambda value: self.label.setText(f"Slider: {value}")
        )
        layout.addWidget(slider)

        # 7. QToolButton
        toolbutton = QToolButton()
        toolbutton.setText("Tool Button")
        toolbutton.clicked.connect(
            lambda: self.label.setText("Tool Button Clicked!")
        )
        layout.addWidget(toolbutton)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = WidgetDemo()
window.show()
sys.exit(app.exec_())




