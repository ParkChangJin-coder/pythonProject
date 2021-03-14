"""
num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))

num = 1
while True:
    if num % num1 == 0 and num % num2 == 0:
        break
    num += 1
print("{0} 과 {1} 의 최소 공배수 : {2}".format(num1,num2,num))


import os

while True:
    os.system("cls")
    num = int(input("출력할 구구단 입력(0 입력 시 종료) : "))
    if num == 0:
        print("구구단을 종료합니다.")
        break
    else:
        i = 1
        while i <= 9:
            print("{0} X {1} = {2}".format(num,i,num*i))
            i+=1
        os.system("pause")
"""

i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i,end=' ')