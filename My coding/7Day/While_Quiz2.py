import random
"""
A = 100
B = 100
print("A의 점수는 {0}, B의 점수는 {1}".format(A,B))
GameCount = int(input("주사위를 몇 번 던지겠습니까?"))
Turn = 1
while Turn <= GameCount:
    AScore = random.randint(1,6)
    BScore = random.randint(1,6)
    print("A의 주사위 : ",AScore)
    print("B의 주사위 : ",BScore)
    print("{0} Round) {1} {2}".format(Turn,AScore,BScore))
    if AScore > BScore:
        B -= AScore
    elif AScore < BScore:
        A -= BScore
    Turn+=1
print("A의 점수는 {0}, B의 점수는 {1}".format(A,B))


Lotte = 0
Samsung = 0
Turn = 1
while Turn <= 12:
    LotteScore = random.randint(0,2)
    SamsungScore = random.randint(0,2)
    print("{0}회) 롯데 삼성 : {1} {2}".format(Turn,LotteScore,SamsungScore))
    if Turn >= 9 and Lotte != Samsung:
        break

    Lotte += LotteScore
    Samsung += SamsungScore
    Turn +=1
if Lotte > Samsung:
    WinTeamName = "롯데"
else:
    WinTeamName = "삼성" 
print("[{0} : {1}] {2}가 승리를 기록했습니다".format(Lotte,Samsung,WinTeamName))
"""

MaxTurn = int(input("대결 횟수 : "))
Turn = 1
while Turn <= MaxTurn:
    Count = int(input("{0}회차 비교 학교 수 : ".format(Turn)))
    University = {}
    i = 1
    while i <= Count: 
        Name = input("대학 이름 : ")
        Num = int(input("술 소비 : "))
        University[Num] = Name
        i+=1
    MaxNum = max(list(University.keys()))
    print("{0}회차 승리 : {1}".format(Turn,University[MaxNum]))
    Turn+=1
    