# Drawing Shapes with QPainter
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QRect


class DrawingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Drawing API")
        self.setGeometry(200, 150, 650, 450)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Enable smooth drawing
        painter.setRenderHint(
            QPainter.Antialiasing
        )

        # 1. Draw a line
        pen = QPen(QColor("blue"), 4)
        painter.setPen(pen)
        painter.drawLine(30, 40, 250, 40)

        # 2. Draw a rectangle
        painter.setPen(QPen(QColor("red"), 3))
        painter.setBrush(QBrush(QColor("pink")))
        painter.drawRect(QRect(40, 80, 150, 90))

        # 3. Draw a circle
        painter.setPen(QPen(QColor("green"), 3))
        painter.setBrush(QBrush(QColor("lightgreen")))
        painter.drawEllipse(250, 80, 120, 120)

        # 4. Draw text
        painter.setPen(QPen(QColor("black")))
        painter.drawText(
            40, 230, "Welcome to PyQt5 Drawing!"
        )

        # 5. Draw another filled rectangle
        painter.setPen(QPen(QColor("purple"), 2))
        painter.setBrush(QBrush(QColor("yellow")))
        painter.drawRect(40, 270, 200, 70)

        painter.end()


app = QApplication(sys.argv)

window = DrawingWindow()
window.show()

sys.exit(app.exec_())
