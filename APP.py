import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.request


class Download(QDialog):
    def __init__(self):
        super().__init__()  # Using `super()` is cleaner

        # Create the layout
        layout = QVBoxLayout()

        # Create and configure the widgets
        self.url_label = QLabel("URL:")
        self.url = QLineEdit(placeholderText="URL")

        self.save_location_label = QLabel("Save Location:")
        self.save_location = QLineEdit(placeholderText="File Save Location")

        browse_button = QPushButton("Browse")
        self.progress = QProgressBar(value=0, alignment=Qt.AlignHCenter)

        download_button = QPushButton("Download")

        # Add widgets to layout
        layout.addWidget(self.url_label)
        layout.addWidget(self.url)
        layout.addWidget(self.save_location_label)
        layout.addWidget(self.save_location)
        layout.addWidget(browse_button)
        layout.addWidget(self.progress)
        layout.addWidget(download_button)

        self.setLayout(layout)

        # Configure dialog window
        self.setWindowTitle("Pydownloader")
        self.setFocus()

        # Connect signals to methods
        download_button.clicked.connect(self.download)
        browse_button.clicked.connect(self.browse_file)

    def browser_file(self):
        save_file = QFileDialog.getSaveFileName(
            self, caption="Save File As", directory=".", filter="All Files(*.*)")
        self.save_location.setText(QDir.toNativeSeparators(str(save_file)))

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        print(save_location)
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "warning", "The Download failed")
            return
        QMessageBox.information(self, "Information",
                                "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum*blocksize
        if totalsize > 0:
            percent = readsofar*100/totalsize
            self.progress.setValue(percent)


app = QApplication(sys.argv)
dialog = Download()
dialog.show()
app.exec_()
