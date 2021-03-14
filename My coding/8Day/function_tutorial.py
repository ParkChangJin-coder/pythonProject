"""
#숫자 하나를 보내줄 경우 해당 숫자의 2배 + 1 한 값을
#돌려주는 기능
def func(x):
    y = x * 2 + 1
    return y

result = func(2)
print("resunt : ",result)
result = func(3)
print("resunt : ",result)

#함수에 정수 2개를 보내서 두 정수의 평균을 돌려주는 기능
def avg(x,y): # avg : 함수명, (x,y) : 매개변수
    result = (x + y) / 2 # 종속문장
    return result#return : 반환 값
print(avg(10,20))#avg(10,20) : 함수호출
print(avg(30,50))

def avg2():
    x = int(input("정수1 입력 : "))
    y = int(input("정수2 입력 : "))
    result = (x + y) / 2
    print("{0} 과 {1}의 평균 값 : {2}".format(x,y,result))
avg2()
avg2()
"""

def total(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    print("sum = ",sum)

total(10)
total(50)
total(100)

def odd_even(num):
    if num % 2 == 0:
        print("짝수 입니다.")
    else:
        print("홀수 입니다.")
odd_even(10)
odd_even(9)

