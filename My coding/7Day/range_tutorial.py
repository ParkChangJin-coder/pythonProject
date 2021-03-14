print(range(5))
print(list(range(5)))
print(tuple(range(5)))

for i in range(10):
    print("i = ",i)
for i in range(5,10):
    print("i = ",i)
#1 ~ 10사이의 모든수의 누적합계
sum = 0
for i in range(1,11):# 1 ~ 10
    sum += i
print("sum = ",sum)

#1 ~ 100 사이의 홀수들의 총합계
sum = 0
for i in range(1,101,2):#1 ~ 100 사이에서 1부터 2씩 증가하는 수
    print(i,end =" ")
    sum += i
print("\nsum = ",sum)
#1 ~ 100 사이의 5의배수 총 합계
sum = 0
for i in range(5,101,5):#5 ~ 100 사이에서 5씩증가 하는 수
    print(i,end=" ")
print()
#100 ~ 1 까지 짝수들 감소
for i in range(100,1,-2):
    print(i,end=" ")
