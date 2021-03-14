"""
def totalSum(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

def x3(num):
    if num % 3 == 0:
        print("{0}는 3의 배수가 맞습니다.".format(num))
    else:
        print("{0}는 3의 배수가 아닙니다.".format(num))

def BigNum():
    num = int(input("정수1 입력 : "))
    num2 = int(input("정수2 입력 : "))
    if num > num2:
        return num
    else:
        return num2

def Abs():
    num = int(input("정수 입력 : "))
    if num >= 0:
        print("{0}의 절대값은 {0}입니다.".format(num))
    else:
        print("{0}의 절대값은 {1}입니다.".format(num,-num))
    
sum = totalSum(10)#10 : 인자값
print("sum = ",sum)
sum = totalSum(30)#10 : 인자값
print("sum = ",sum)
sum = totalSum(50)#10 : 인자값
print("sum = ",sum)

x3(10)
x3(9)

print(BigNum())
print(BigNum())

Abs()


def ChangeName():
    Name = input("이름 입력 : ")
    index = Name.find(" ")
    FirstName = Name[:index]
    LastName = Name[index:]
    return LastName+" "+FirstName

Name = ChangeName()
print(Name)


def ListCheck(List):
    List = list(List)
    ResultList = []
    for i in List:
        if i >= 5:
            ResultList.append(i)
    return ResultList

List = [12,6,3,8,7,2,4,9,1]
print(ListCheck(List))

# 123 -> 3 -> 2 -> 1
def Reverse(Num):
    while Num != 0:
        print(Num%10,end="")
        Num //=10
Reverse(12345)
""" 
import os
def sum(x,y):
    print("{0} + {1} = {2}".format(x,y,x+y))
def sub(x,y):
    print("{0} - {1} = {2}".format(x,y,x-y))
def mul(x,y):
    print("{0} x {1} = {2}".format(x,y,x*y))
def divi(x,y):
    print("{0} / {1} = {2}".format(x,y,x/y))

while True:
    os.system("cls")
    a,b = map(int,input("숫자를 두개 입력하세요 : ").split())
    print("계산할 방식을 선택하세요")
    print("1.더하기")
    print("2.빼기")
    print("3.곱하기")
    print("4.나누기")
    print("5.종료")
    Select = int(input("입력 : "))
    if Select == 1:
        sum(a,b)
    elif Select == 2:
        sub(a,b)
    elif Select == 3:
        mul(a,b)
    elif Select == 4:
        divi(a,b)
    elif Select == 5:
        break
    else:
        print("잘못 입력하셧습니다.")
    os.system("pause")

