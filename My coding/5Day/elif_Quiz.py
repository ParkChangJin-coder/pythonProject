"""
Kor,Eng,Math = map(int,input("국어,영어,수학 점수 입력").split())
Sum = Kor + Eng + Math
Avg = Sum / 3

if Avg >= 90:
    Class = 'A'
elif  Avg >=80:
    Class = 'B'
elif Avg >= 70:
    Class = 'C'
elif Avg >= 60:
    Class = 'D'
else:
    Class = 'F'
print("{0}등급".format(Class))


Count = input("입력 : ")
ACount = Count.count("A") + Count.count("a") 
BCount = Count.count("B") + Count.count("b")
print("A는 {0}표, B는 {1}표".format(ACount,BCount))

if ACount > BCount :
    print("우승자는 A 입니다.")
elif ACount < BCount :
    print("우승자는 B 입니다.")
else:
    print("무승부 입니다.")


"""
ManduCount = int(input("만두 개수를 입력하세요 : "))

Price = ManduCount * 1000

if ManduCount >= 100:
    Price *= 0.75
elif ManduCount >= 10:
    Price *= 0.85
print("가격 : {0}원,현금결제가 : {1}원".format(int(Price),int(Price * 0.9)))

"""
BirthNumber = input("주민번호 7자리 입력 : ")
Birth = BirthNumber[:-2]
GenderNumber  = BirthNumber[-1]
print("생년월일 6자리 : ",Birth)
print("주민번호 뒷자리의 첫글자 : ",GenderNumber)
if GenderNumber == '1' or GenderNumber == '2':
    BirthYear = "19" + BirthNumber[:2]
elif GenderNumber == '3' or GenderNumber == '4':
    BirthYear = "20" + BirthNumber[:2]
print("성별정보가 {0}이므로, {1}년생, {2}살입니다.".format(GenderNumber,BirthYear,2021 - int(BirthYear) + 1))
"""

Minute = int(input("주차한 시간을 입력하세요 : "))

Price = 1000
if Minute > 30:
    Minute -= 30
    Price +=(Minute // 10 * 500)
    if Minute % 10 != 0:
        Price += 500

print("주차요금은 {0}원입니다.".format(Price))