"""
def WordQuiz(WordDic):
    WordDic = dict(WordDic)
    Word = input("단어입력 : ")
    if Word in WordDic.keys():
        print("{0} : {1}".format(Word,WordDic[Word]))
    else:
        print("해당 단어가 존재하지 않습니다.")

WordDic = {"apple":"사과","banana":"바나나","cat":"고양이","dinosaur":"공룡","elephant":"코끼리"}
WordQuiz(WordDic)
WordQuiz(WordDic)
WordQuiz(WordDic)
WordQuiz(WordDic)

#123T
#25G
def ChangeByte(Data):
    Data = str(Data)
    Type = Data[-1]
    Data = int(Data[:-1])
    if Type == 'T':
        return Data * 1024 * 1024 * 1024 * 1024
    elif Type == 'G':
        return Data * 1024 * 1024 * 1024
    elif Type == 'M':
        return Data * 1024 * 1024
    elif Type == 'K':
        return Data * 1024
    else: return Data

print(ChangeByte('3T'),"byte")
print(ChangeByte('2G'),"byte")
print(ChangeByte('5M'),"byte")
print(ChangeByte('4K'),"byte")

def login(id,pw,account):
    account = dict(account)
    id = str(id)
    pw = str(pw)
    if id not in account.keys():
        print("해당 아이디가 존재하지 않습니다.")
    else:
        if account[id] != pw:
            print("비밀번호가 일치하지 않습니다.")
        else:
            print("[{0}]님이 로그인 하셧습니다.".format(id))


account = {"itbank":"it"}
id = input("아이디 : ")
pw = input("비밀번호 : ")
login(id,pw,account)


def avg_score(**Score):
    sum = 0
    for key in Score.keys():
        print("과목명 {0} : {1}점".format(key,Score[key]))
        sum += Score[key]
    print("평균 : {0}".format(sum/ len(Score.keys())))

avg_score(A=100,B=80,C=75)
avg_score(A=100,B=80,C=75,D=99,E=53)
def My_Avg(*Num):
    print(sum(Num) / len(Num))
def My_Max(*Num):
    print(max(Num))

My_Avg(5,3,7,8,4,2)
My_Max(5,3,7,8,4,2)
"""
import random
def LottoCheck(*LottoList):
    AnswerLotto = []
    while len(AnswerLotto) < 6:
        AnswerLotto.append(random.randint(1,45))
        AnswerLotto = set(AnswerLotto)
        AnswerLotto = list(AnswerLotto)
    count = 0
    print(AnswerLotto)
    print(LottoList)
    for i in LottoList:
        if i in AnswerLotto:
            count += 1
    print("맞춘 숫자 갯수 : ",count)
LottoCheck(23,33,14,17,21,29)