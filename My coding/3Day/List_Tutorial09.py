a = "Hello Java World"
print(a.split())

jumsu = [100,85,87,99,35,64]
print(jumsu)
print(jumsu[1] + jumsu[3])

student = ["kim","lee","park"]
print(student)
print(student[2])
print(student[2][-1])

a = [1,2,3,['a','b','abc']]
print(a[0])
print(a[3])
#print(a[4])
print(a[-1])
print(a[3][1])
print(a[3][2])
print(a[3][2][2])

#1.2데이터를 index로 가져와 출력
a = [1,2,["Python",['c','b'],[1.2,"itbak",5.55],5]]
print(a[2][2][0])

a = [1,2,3,4,5]
print(a[1:-1])
print(a[:3])
print(a[2:])

a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

a = [1,2,3,4,5,6,7,8,9,10]
print(a[::2])
print(a[1::2])

a = [1,2,3]
b = [4,5,6]
#list 간에 + 연산은 두 개의 list 합치는 연산
c = a + b
print(c)
a = "123"
b = "456"
print(a + b)
print(a * 3)
a = [1,2,3]
d = a * 3
print(d)

#list는 같은 list끼리 연산이 가능하다.
a = [10,20,30]
print(str(a) + "KKK")

#문자열은 index로 데이터 변경이 불가능 하다.
#a = "Hello"
#a[1] ='a'# Hello -> Hallo
#print(a)
a = [1,2,3]
print(a)
a[2] = 4
print(a)

#슬라이싱으로 일정 범위의 list 데이터를 변경 시
#하나의 list 데이터들이 추가된다.
a = [1,2,3,4,5,6,7]
print(a)
a[2:4] = [10,20,30]
print(a)

#index 로 list 를 수정 시 중첩 list 형으로 추가된다.
a = [1,2,3,4,5,6,7]
print(a)
a[2] = [10,20,30]
print(a)

#슬라이싱으로 빈 list 로 수정 시 해당 범위의 데이터가 삭제된다.
a = [1,2,3,4,5]
print(a)
a[1:4] = []
print(a)

#index로 특정 데이터 삭제 시 빈 list 넣으면
#삭제가 아닌 빈 list로 변경이 이루어진다
a = [1,2,3,4,5]
print(a)
a[2] =[]
print(a)

#del : 특정 객체를 삭제할때 사용한다.
a = [1,2,3,4,5]
print(a)
del a[2]
print(a)

a = [1,2,3,4,5]
print(a)
#a[1:4] = []
del a[1:4]
print(a)

#일반 변수도 del로 삭제가 가능하다.
a = 10;
print(a)
del a
#print(a)

#문자열은 전체를 삭제할 순 있으나.
#특정 위치의 단일문자만 삭제할 순 없다.
st = "ITBANK"
#del st[1]
del st

#max 함수
#max : list내에 숫자 중 가장 큰 수를 찾아온다.
a = [1,2,3,4,5,10,6,7,8]
print(max(a))
#min : list내에 숫자 중 가장 작은 수를 찾아온다.
print(min(a))