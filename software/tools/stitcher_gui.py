import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
from functools import partial
from script_stitch_slide import stitch_slide_from_path


import os
os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

class StitcherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slide Stitcher")
        self.setGeometry(100, 100, 400, 300)

        self.slide_path_label = QLabel("Slide Path:", self)
        self.slide_path_label.setGeometry(20, 20, 100, 30)

        self.slide_path_edit = QLineEdit(self)
        self.slide_path_edit.setGeometry(130, 20, 200, 30)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setGeometry(340, 20, 50, 30)
        self.browse_button.clicked.connect(self.browse_slide)

        self.stitch_button = QPushButton("Stitch", self)
        self.stitch_button.setGeometry(150, 250, 100, 30)
        self.stitch_button.clicked.connect(self.stitch_slide)

    def browse_slide(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Slide Folder")
        if folder_path:
            self.slide_path_edit.setText(folder_path)

    def stitch_slide(self):
        slide_path = self.slide_path_edit.text().strip()
        if not slide_path:
            QMessageBox.critical(self, "Error", "Please select slide folder.")
            return

        try:
            stitch_slide_from_path(slide_path)
            QMessageBox.information(self, "Success", "Slide stitching completed successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StitcherGUI()
    window.show()
    sys.exit(app.exec_())

