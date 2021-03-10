import os
import random 
# i = 1
# sum = 0
# while i <= 1000:
#     if i % 3 !=0 or (i % 3 == 0 and i % 5 == 0):
#         sum += i
#     i+=1
# print("sum = ",sum)

# Menu = {"콜라":1200, "사이다":1200, "조지아":1000, "컨피던스":600}
# Money = int(input("돈을 넣으세요 : "))
# while True:
#     os.system("cls")
#     print("잔돈 {0}".format(Money))
#     print("==========자판기==========")
#     j = 0
#     keyList = list(Menu.keys())
#     while j < len(keyList):
#         print("{0}\t:\t{1}".format(keyList[j],Menu[keyList[j]]))
#         j += 1
#     print("> 종료")
#     select = input("음료를 선택하세요 : ")
#     if select in keyList:
#         if Money - Menu[select] < 0:
#             print("잔액이 부족합니다")
#             break
#         Money -= Menu[select]
#     elif select == "종료":
#         print("프로그램을 종료합니다.")
#     else:
#         print("잘못된 입력입니다.")
#     os.system("pause")

# point = 0
# wordList = ["itbank","hello","dog", "boy"]
# MaxPoint = len(wordList)
# #random.randrange(4) -> 0 부터 3까지 랜덤수
# #random.randrange(2,5) -> 2 이상 5 미만
# while wordList:
#     index = random.randrange(len(wordList))
#     print(wordList[index][0])
#     Answer = input("단어를 입력")
#     if Answer == wordList[index]:
#         print("정답")
#         point += 1
#     else:
#         print("오답입니다.")
#     del wordList[index]
#     #wordlist.remove(Answer)
# if point == MaxPoint:
#     print("모두 맞췄습니다")
# else:
#     print("{0}개 만큼 맞췄습니다.".format(point))

