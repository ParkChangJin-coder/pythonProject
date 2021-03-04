from tkinter import *
from datetime import datetime
win = Tk()
win.geometry("500x500") #창 크기
win.title("converter") #창 제목
win.option_add("*Font", "맑은고딕 20") #폰트, 글자 크기

def alert():
    d_now = datetime.now() #현재시각
    btn.config(text=d_now) #버튼을 누르면 버튼 안에 현재시각이 나타남

btn = Button(win, text="변환!", ) # 버튼
btn.config(width=10) #버튼 크기
btn.config(command=alert) #함수 사용
btn.pack()

win.mainloop() #창 활성화
