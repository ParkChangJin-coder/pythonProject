"""
num = int(input("정수 입력 : "))

for i in range(num,0,-1):
    print(i,end = " ")


for i in range(4):
    num = int(input("양수 입력 : "))
    if num < 0:
        print("잘못된 입력입니다.")
    elif num == 0:
        print("0은 0입니다.")
    elif num % 2 == 0:
        print("{0}는 짝수입니다.".format(num))
    elif num % 2 == 1:
        print("{0}는 홀수입니다.".format(num)) 

money = 1#돈
sum = 0#통장
for day in range(30):
    sum += money
    money*=2
print("한달 동안 저축한 금액 : ",sum)

num = int(input("정수 입력 : "))
check = True
for i in range(2,num):
    if num % i == 0:
        check = False
        break
if check == True:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")
"""

num = int(input("정수 2개 입력"))
num2 = int(input())
if num < num2:
    min = num
else:
    min = num2
max = 0
for i in range(1,min+1):
    if num % i == 0 and num2 % i == 0:
        print(i,end = " ")
        max = i
print("\n최대 공약수 : ",max)