import sys

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton
import pandas as pd


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
            print(links)

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
            print(links)

            for i in range(len(links)): #링크 안의 숫자만큼 for를 돌린다
               type = links[i].split('.') #링크 안에 "."으로 나누어 csv 문자를 분리한다
               type.reverse() # 링크 리스트를 역정렬한다
               print("type : ", type)
               if type[0] == 'csv': #csv 인지 판별하는 if
                 read_Excel = pd.read_csv(links[i], encoding='UTF8')  #링크 i 번째 를 UTF8로 인코딩
                 frame_Excel = pd.DataFrame(read_Excel)
                 name = type[1].split('/') #디렉토리 '/'로 나누고 파일명을 가져온다
                 name.reverse() #파일명을 가져오기 위해 역정렬
                 print("name : ", name)
                 frame_Excel.to_excel(name[0] + ".xlsx", encoding='UTF-8', index=False)  # index=False로 데이터 앞에 숫자를 출력 안함
               else:
                 print("csv파일이 아닙니다.")
                 print("아힝흥행")

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
