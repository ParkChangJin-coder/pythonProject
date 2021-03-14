# 10 -> 1 ~ 10
'''
num = 1
sum = 0
end = int(input("정수 입력 : "))
while num <= end:
    sum += num
    num += 1
print("Sum = ",sum)


num = 1
while num <= 10:
    print("Hello, Python")
    num += 1


num = 1
sum = 0
while num != 0:
    num = int(input("정수 입력 : "))
    sum += num
print("Sum = ",sum)
'''


num = input("정수 입력 : ")# 123
num = list(num)# ['1','2','3']
num.reverse()# ['3','2','1']
#join list 데이터 사이에 특정 단어를 끼워서 문자로 변환
num = ''.join(num)#['3','2','1'] -> 321
print(num)

num = int(input("정수 입력 : ")) # num = 123

'''
while num != 0:
    print(num % 10,end='') # 123 % 10 -> 3 12 % 10 -> 2 1 % 10 -> 1
    num //= 10# 123 // 10 -> 12 // 10 -> 1 // 10 -> 0

num = int(input("정수 입력 : "))
'''
"""
i = 1
while i <= num:
    print(num * i,end=' ')
    i += 1
"""