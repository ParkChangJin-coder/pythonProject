# def WordQuiz(WordDic):
#     WordDic = dict(WordDic)
#     Word = input("단어 입력 : ")
#     if Word in WordDic.keys():
#         print("{0} : {1}".format(Word,WordDic[Word]))
#     else:
#         print("해당 단어가 존재하지 않습니다.")
    
# WordDic = {"apple":"사과", "banana":"바나나", "cat":"고양이","dinosour":"공룡"}
# WordQuiz(WordDic)

# def Change_Bite(Data):
#     Data = str(Data)
#     Type = Data[-1]
#     Data = int(Data[:-1])
#     if Type == "T":
#         return Data * 1024 * 1024 * 1024 * 1024
#     elif Type == "G":
#         return Data * 1024 * 1024 * 1024
#     elif Type == "M":
#         return Data * 1024 * 1024
#     elif Type == "K":
#         return Data * 1024
#     else:
#         return Data
# print(Change_Bite('3T'),"Byte")
# print(Change_Bite('2G'),"Byte")
# print(Change_Bite('1M'),"Byte")
# print(Change_Bite('6K'),"Byte")
# print(Change_Bite('15B'),"Byte")

# def login(id,pw,account):
#     account = dict(account)
#     id = str(id)
#     pw = str(pw)
#     if id not in account.keys():
#         print("해당 아이디가 존재하지 않습니다.")
#     else:
#         if account[id] != pw:
#             print("비밀번호가 일치하지 않습니다.")
#         else:
#             print("{0}님이 로그인 하셨습니다".format(id))

# account = {"itbank":"it"}
# id = input("아이디 : ")
# pw = input("비번 : ")

# login(id,pw,account)

# def avg_score(**Score):
#     sum = 0
#     for key in Score.keys():
#         print("과목명 {0} : {1}점".format(key,Score[key]))
#         sum += Score[key]
#     print("평균 : {0}".format(sum/len(Score.keys())))
# avg_score(A=100,B=95,C=50)
# avg_score(A=50,B=80)

import random

def Lotto_Check(*LottoList):
    AnswerLotto = []
    while len(AnswerLotto):
        AnswerLotto.append(random.randint(1,45))
        AnswerLotto = set(AnswerLotto)
        AnswerLotto = list(AnswerLotto)
    count = 0
    print(AnswerLotto)
    print(LottoList)
    for i in LottoList:
        if i in AnswerLotto:
            count += 1
    print("맞춘 숫자 개수 : ", count)

Lotto_Check(12,25,37,46,9,1)
