"""
def total(*args):
    sum = 0
    for i in args:
        sum += i
    print("sum = ",sum)

def calc(oper,*v):
    if oper == '+':
        sum = 0
        for i in v:
            sum += i
    elif oper == '*':
        sum = 1
        for i in v:
            sum *= i
    print("sum = ",sum)

def dict_Change(**Dic):
    print(Dic)
dict_Change(rank1 = 'Java',rank2 ='C',rank3 = 'C++',rank4 = 'Python')

total(1,2,3,4,5,6,7,8,9,10)
total(10,11,12,13)

calc('+',1,2,3,4,5)
calc('*',2,4,6,8)
#디폴트 매개변수(default parameter)
def TestReturn(a,b = 10):
    return a * b
    return a + b
print(TestReturn(2))
print(TestReturn(2,5))
"""

a = 10
def test():
    global a
    a += 10
    print("함수 내부 a : ",a)

print("함수 호출전 a : ",a)
test()
print("함수 호출후 a : ",a)
#lambda : 익명의 함수
sum = lambda a,b:a+b
print(sum(10,20))
