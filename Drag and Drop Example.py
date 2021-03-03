import sys

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
                self.addItems(links)
        else:
            event.ignore()


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 600)

        self.lstbox_view = ListBoxWidget(self)

        self.btn = QPushButton("Get Value", self)
        self.btn.setGeometry(50, 400, 200, 50)

        self.btn.clicked.connect(lambda: print(self.getSelectedItem()))

    def getSelctedItem(self):
        item = QListWidgetItem(self.lstbox_view.currentItem())
        return item.text()


app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())
