# Brush Style Constants in PyQt5


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt


class BrushDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Brush Styles")
        self.setGeometry(200, 150, 650, 450)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        brush_styles = [
            ("Solid", Qt.SolidPattern),
            ("Horizontal", Qt.HorPattern),
            ("Vertical", Qt.VerPattern),
            ("Cross", Qt.CrossPattern),
            ("Diagonal", Qt.FDiagPattern),
            ("Diagonal Cross", Qt.DiagCrossPattern),
            ("Dense 1", Qt.Dense1Pattern),
            ("Dense 4", Qt.Dense4Pattern),
            ("Dense 7", Qt.Dense7Pattern),
        ]

        x = 30
        y = 50

        for index, (name, style) in enumerate(brush_styles):
            painter.setPen(QPen(Qt.black, 1))

            # Create a brush with the selected style
            brush = QBrush(QColor("lightblue"), style)
            painter.setBrush(brush)

            # Draw the rectangle
            painter.drawRect(x, y, 170, 65)

            # Write the pattern name
            painter.drawText(x, y - 10, name)

            x += 210

            # Move to the next row after three rectangles
            if (index + 1) % 3 == 0:
                x = 30
                y += 120

        painter.end()


app = QApplication(sys.argv)
window = BrushDemo()
window.show()
sys.exit(app.exec_())


