from tkinter import *
# from datetime import datetime
win = Tk()
win.geometry("200x100") #창 크기
win.title("ALERT!") #창 제목
win.option_add("*Font", "맑은고딕 10") #폰트, 글자 크기

def quit():
    win.quit()
    win.destroy()

    # d_now = datetime.now() #현재시각
    # btn.config(text=d_now) #버튼을 누르면 버튼 안에 현재시각이 나타남

btn = Button(win, text="파일 형식을 확인해 주세요") # 버튼
btn.config(width=25) #버튼 크기
# btn.config(command=quit()) #함수 사용
btn.pack()

win.mainloop() #창 활성화
