a = "Hello java world"
print(a.split())

jumsu = [100, 85, 70, 65, 30]
print(jumsu)
print(jumsu[1] + jumsu[3])

student = ["kim", "Lee", "Park"]
print(student)
print(student[1])
print(student[2][-1])
print("")
a = [1, 2, 3,['a','b','abc']]
print(a[0])
print(a[3])
print(a[3][1])
print(a[3][2][2])
print("")
a = [1, 2, ["Python", ['c', 'b'], [1.2, "itbank",5.55],5]]
print(a[2][2][1][3])
print(a[2][2][0])
print("")
a = [1,2,3,4,5]
print(a[1:-1])

a = [1, 2, 3, ['a','b','c'], 4, 5]
print(a[2:5])
print(a[3][:2])
a = [1,2,3,4,5,6,7,8,9,10]
print(a[::2])
print(a[1::3])
print("")
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print("")
print(a*2)
print("")
# a=[10,20,30]
# print(a + "iii") 불가능

# a = "Hello" 이것도 불가능
# a[1] = 'a'
# print(a)

a = [1,2,3] #변경 가능
a[2] = 4
print(a)
print("")
a = [1,2,3,4,5,6,7]
print(a)
a[2:4] = [10,20,30] #데이터 추가 및 편집
print(a)
a[2:5] = []
print(a)
print("")
#index 로 list수정시 중첩 list 형으로 추가된다
a = [1,2,3,4,5,6,7]
a[1:4] = []
print(a)
print("")
a = [1,2,3,4,5,6,7]
print(a)
a[2] = [] #빈 리스트로 변경 됨
print(a)
print("")
a = [1,2,3,4,5,6,7]
print(a)
del a[2] #삭제 
print(a)
print("")
a = [1,2,3,4,5,6,7]
print(a)
del a[2:4]
print(a)
print("")
# a = 10
# print(a)
# del a
# print(a)

# st = "ITBANK" 불가능
# del st[1]
# print(st)
# del st 는 가능

#max(), min()
a = [1,2,3,4,5,6,7]
print(max(a), min(a))
print("")
a = [10, 22, 33, 44, 50]
a[1:-1] = [20, 30, 40]
print(a)

b = [21, 9, 12, 17, 9, 3 ,27, 32, 1]
print(b)
b[2] = 22
b[3] = 7
b[-2] = 19
print(b)
print(b[::2])
print(b[1::2])

Sum1 = sum(b[::2])
Sum2 = sum(b[1::2])
print(Sum1, Sum2)

c = [5, 9, 1, 2, 10, 15]
print(max(c), min(c))
