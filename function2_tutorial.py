# def total(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print("sum = ", sum)
# total(1,2,3,4,5,6,7)
# total(2,4,5,6,7,8)

# def calc(oper,*v):
#     if oper == "+":
#         sum = 0
#         for i in v:
#             sum += i
#     elif oper == "*":
#         sum = 1
#         for i in v:
#             sum *= i
#     print("sum = ", sum)
# calc("+",1,2,3,4,5)
# calc("*",1,2,3,4)

# def dict_change(**Dic):
#     print(Dic)

# dict_change(rank1 = 'java', rank2 = 'C++', rank3 = 'python')

# def TestReturn(a,b=10):
#     return a * b
# print(TestReturn(2), "한개")
# print(TestReturn(2,5), "두개")

a = 10
def Test():
    a = 20
    print("함수 내부 a: ", a)
print("호출 전 a : ", a)
Test()
print("호출 후 a : ", a)

a = 10
def Test(): #global => 외부에 있는 변수 호출가능
    global a
    a += 10
    print("함수 내부 a: ", a)
print("호출 전 a : ", a)
Test()
print("호출 후 a : ", a)

