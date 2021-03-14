a = [10,22,33,44,50]
print(a)
a[1:4] = [20,30,40]
print(a)
del a[2]
print(a)


b = [21,9,12,17,9,3,27,32,1]
print(b)
b[-2] = 19
b[2:4]= [22,7]
print(b)
even = b[0] + b[2] + b[4] + b[6] + b[8]
odd = b[1] + b[3] + b[5] + b[7]
print("짝수 합 : ", even)
print("홀수 합 : ", odd)
print("sum = ",sum(b))
#sum : list 안의 모든 데이터 총 합을 구해주는 기능
print("짝수 합 : ", sum(b[::2]))
print("홀수 합 : ", sum(b[1::2]))

c = [5,9,1,2,10,15]
#max : list 안의 데이터 중 가장 큰 수를 반환
#min : list 안의 데이터 중 가장 작은 수를 반환
print("Max : ",max(c))
print("Min : ",min(c))