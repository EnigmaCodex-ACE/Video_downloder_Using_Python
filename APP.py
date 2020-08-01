import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.request


class Download(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        l1 = QLabel()
        l1.setText("URL:")
        self.url = QLineEdit()
        l2 = QLabel()
        l2.setText("Save Location:")
        self.save_location = QLineEdit()
        browse = QPushButton("Browse")
        self.progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File Save Location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(l1)
        layout.addWidget(self.url)
        layout.addWidget(l2)

        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        
        self.setWindowTitle("Pydownloader")
        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browser_file)

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
