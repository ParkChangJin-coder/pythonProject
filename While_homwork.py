import os
import random

i = 1
Lotte_Score = 0
Samsung_Score = 0

while i < 10:
    Lotte_Score1 = random.randint(0, 2)
    Samsung_Score1 = random.randint(0, 2)
    print("{0}회) 롯데 삼성 {1} : {2}".format(i, Lotte_Score1, Samsung_Score1))
    i += 1
    Lotte_Score += Lotte_Score1
    Samsung_Score += Samsung_Score1

if Lotte_Score > Samsung_Score:
    Winner = "롯데"
elif Lotte_Score < Samsung_Score:
    Winner = "삼성"
elif Lotte_Score == Samsung_Score:
    while i < 13:
            Lotte_Score1 = random.randint(0, 2)
            Samsung_Score1 = random.randint(0, 2)
            print("{0}회) 롯데 삼성 {1} : {2}".format(i, Lotte_Score1, Samsung_Score1))
            i += 1
            Lotte_Score += Lotte_Score1
            Samsung_Score += Samsung_Score1
            if Lotte_Score != Samsung_Score:
                if Lotte_Score > Samsung_Score:
                    Winner = "롯데"
                elif Lotte_Score < Samsung_Score:
                    Winner = "삼성"
                break

print("[{0} : {1}] {2}이(가) 승리하였습니다.".format(Lotte_Score, Samsung_Score, Winner))