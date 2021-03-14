"""
i = 1
sum = 0
while i <= 1000:
    if i % 3 != 0 or i % 15 == 0:
        sum += i
    i+=1
print("합계 : ",sum)

import os
Menu = {"콜라":1200,"사이다":1200,"조지아":1000,"컨피던스":600}

Money = int(input("돈을 넣으세요 : "))

KeyList = list(Menu.keys())
print(KeyList)
while True:
    os.system("cls")
    print("잔돈 : {0}".format(Money))
    print("========자판기========")
    j = 0
    while j < len(KeyList):
        print(" {0}:{1}원".format(KeyList[j],Menu[KeyList[j]]))
        j+=1
    print("> 종료")
    Select = input("음료를 선택하세요")
    if Select in KeyList:
        if Money - Menu[Select] < 0:
            print("잔액이 부족합니다.")
            break
        else:
            Money -= Menu[Select]
    elif Select == "종료":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")
    os.system("pause")
"""
import random
#0 ~ 3
wordlist = ["itbank","hello","dog","boy"]
#len(wordlist) -> 4
#random.randrange(4) -> 0 부터 4미만까지의 랜덤 수를 가져온다.
#random.randrange(2,5) -> 2 ~ 4
point = 0
MaxPoint = len(wordlist)# 4
while wordlist:  
    print(wordlist) 
    index = random.randrange(len(wordlist))# 0 부터 4미만 사이 수
    print(wordlist[index][0])
    Answer = input("단어를 입력 : ")
    if  Answer == wordlist[index]:
        print("정답입니다!")
        point += 1
    else:
        print("오답입니다..")
    del wordlist[index] #index로 삭제
    #wordlist.remove(Answer) # 데이터로 삭제
if point == MaxPoint:
    print("모두 맞췄습니다!!")
else:
    print("{0}개 맞췄습니다.".format(point))

