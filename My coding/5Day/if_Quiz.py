"""
num = int(input("정수 입력 : "))
if num % 5 == 0:
    print("5의 배수 입니다.")
else:
    print("5의 배수가 아닙니다.")

num = int(input("정수 입력 : "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

num1,num2 = map(int,input("정수 두 개 입력 : ").split())

if num1 % num2 == 0:
    print("{0}은 {1}의 배수입니다.".format(num1,num2))
else:
    print("{0}은 {1}의 배수가 아닙니다.".format(num1,num2))


num1,num2 = map(int,input("정수 두 개 입력 : ").split())

if num1 > num2:
    if num1 % 2 == 0:
        print("큰수 인 {0}은 짝수입니다.".format(num1))
    else:
        print("큰수 인 {0}은 홀수입니다.".format(num1))
else:
    if num2 % 2 == 0:
        print("큰수 인 {0}은 짝수입니다.".format(num2))
    else:
        print("큰수 인 {0}은 홀수입니다.".format(num2))


num1,num2 = map(int,input("정수 두 개 입력 : ").split())
sum = num1 + num2
if sum % 2 == 0 and sum % 3 == 0:
    print("3의배수 이며 짝수 입니다.")
else:
    print("조건에 부합하지 않습니다.")

num = int(input("정수 입력 : "))

if num < 0:
    print("{0}의 절대값 : {1}".format(num,-num))
else:
    print("{0}의 절대값 : {1}".format(num,num))

Year,Month,Day = map(int,input("년 월 일 입력 : ").split())
Answer = Year - Month + Day
if Answer % 10 == 0: # % 10 -> 해당 숫자의 1의자리를 가져올 수 있다.\
    print("대박")
else:
    print("그럭저럭") 

StationCount = int(input("정거장 수 : "))
CountMinute = 0
if StationCount >= 10:
    CountMinute = 4
else:
    CountMinute = 2

TotalMinute = StationCount * CountMinute

print("총 소요 시간은 {0}시간 {1}분 입니다.".format(TotalMinute // 60,TotalMinute % 60))

A = 5
B = 7
Num = int(input("현재 층 입력 : "))
#abs : 절대값을 구해주는 기능
AbsA = abs(Num - A)
AbsB = abs(Num - B)
if AbsA < AbsB:
    print("A엘리베이터가 움직입니다.")
else:
    print("B엘리베이터가 움직입니다.")


MyDic = {"Money":"돈","Monkey":"원숭이","Apple":"사과"}
Key = input("영어 단어 입력 : ")
if Key in MyDic:
    Value = input("영어 단어 뜻 입력 : ")
    if Value == MyDic[Key]:
        print("정답입니다.")
    else:
        print("틀렸습니다.")
else:
    print("해당 단어가 없습니다.")
"""