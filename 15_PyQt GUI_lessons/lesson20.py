# QPixmap in PyQt5


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFileDialog,
    QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 QPixmap Image Viewer")
        self.setGeometry(200, 100, 750, 550)

        self.original_pixmap = QPixmap()

        # Image display area
        self.image_label = QLabel("Open an image to begin")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(400, 300)
        self.image_label.setStyleSheet(
            "QLabel { background-color: #eeeeee; "
            "border: 1px solid gray; }"
        )

        # Buttons
        open_btn = QPushButton("Open Image")
        fit_btn = QPushButton("Fit Image")
        save_btn = QPushButton("Save Image As")

        button_layout = QHBoxLayout()
        button_layout.addWidget(open_btn)
        button_layout.addWidget(fit_btn)
        button_layout.addWidget(save_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label, 1)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Connect button events
        open_btn.clicked.connect(self.open_image)
        fit_btn.clicked.connect(self.fit_image)
        save_btn.clicked.connect(self.save_image)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif);;"
            "All Files (*.*)"
        )

        if not file_path:
            return

        pixmap = QPixmap(file_path)

        if pixmap.isNull():
            QMessageBox.warning(
                self, "Error",
                "The selected file could not be loaded as an image."
            )
            return

        self.original_pixmap = pixmap
        self.fit_image()

    def fit_image(self):
        if self.original_pixmap.isNull():
            QMessageBox.information(
                self, "Information",
                "Please open an image first."
            )
            return

        scaled_pixmap = self.original_pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.image_label.setPixmap(scaled_pixmap)

    def save_image(self):
        if self.original_pixmap.isNull():
            QMessageBox.warning(
                self, "Warning", "No image to save."
            )
            return

        file_path, selected_filter = QFileDialog.getSaveFileName(
            self,
            "Save Image As",
            "image.png",
            "PNG Image (*.png);;JPEG Image (*.jpg *.jpeg);;"
            "BMP Image (*.bmp)"
        )

        if not file_path:
            return

        # Add an extension if the user omitted one
        if not file_path.lower().endswith(
            (".png", ".jpg", ".jpeg", ".bmp")
        ):
            if "JPEG" in selected_filter:
                file_path += ".jpg"
            elif "BMP" in selected_filter:
                file_path += ".bmp"
            else:
                file_path += ".png"

        if self.original_pixmap.save(file_path):
            QMessageBox.information(
                self, "Saved", "Image saved successfully!"
            )
        else:
            QMessageBox.warning(
                self, "Error", "Could not save the image."
            )


app = QApplication(sys.argv)
window = ImageViewer()
window.show()
sys.exit(app.exec_())
