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

            links = [] #파일의 주소를 저장한다.
            print(links)

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
            print(links)
            #과제 1 : 변환 if문을 class 문으로 깔끔하게 호출할 수는 없을까?
            #과제 2 : 생성되는 csv, 엑셀 파일이 같은 이름의 파일이 존재할 때 이름 뒤에 (1), (2)등을 붙이기
            #과제 3 : 헤더 수와 열의 수가 맞지 않을 경우 에러 메세지를 띄우는 방법
            for i in range(len(links)): #링크 안의 데이터 수 만큼 for를 돌린다
               type = links[i].split('.') #파일주소와 파일명을 "."으로 나누어 csv 확장자를 분리한다
               type.reverse() # 파일 주소를 역정렬해서 확장자를 맨 앞으로 배치한다.
               if type[0] == 'csv': #csv 인지 판별하는 if
                 read_Excel = pd.read_csv(links[i], encoding='UTF8')  #링크 i 번째 를 UTF8로 인코딩
                 frame_Excel = pd.DataFrame(read_Excel)
                 name = type[1].split('/') #파일 주소를 '/'로 나눈다
                 name.reverse() #파일명이 맨 앞으로 오도록 리스트 역정렬
                 frame_Excel.to_excel(name[0] + ".xlsx", encoding='UTF-8', index=False)  # index=False로 데이터 앞에 숫자를 출력 안함
               elif type[0] == 'xlsx': #엑셀 파일 인지 판별하는 if
                   read_Csv = pd.read_excel(links[i])
                   frame_csv = pd.DataFrame(read_Csv)
                   name = type[1].split('/')  # 파일 주소를  '/'로 나눈다
                   name.reverse()  # 파일명이 앞으로 오도록 리스트 역정렬
                   frame_csv.to_csv(name[0] + ".csv", encoding='UTF-8-sig', index=False)
               else:
                 print("파일 형식을 확인해 주세요")

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
