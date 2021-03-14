# def func(x):
#     y = x * 2 + 1
#     return y

# result = func(2)
# print("result2 = ",result)
# result = func(3)
# print("result3 = ",result)

# def avg(x,y):
#     result = (x + y) /2
#     return result

# print(avg(10,20))
# print(avg(30,40))

# def avg2():
#     x = int(input("정수1입력 : "))
#     y = int(input("정수2입력 : "))
#     result = (x + y) / 2
#     print("{0}과 {1}의 평균값 : {2}".format(x,y,result))
# avg2()

def total(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print("sum = ", sum)
total(10)
total(50)
total(100)

