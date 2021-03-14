# def totalSum(num):
#     sum = 0
#     for i in range(1,num+1):
#         sum+=i
#     return sum #반환값
# sum = totalSum(10) #입력값 10 -> 인자값
# print(sum)

# def odd(num):
#     if num % 3 == 0:
#         print("3의 배수 입니다.")
#     else:
#         print("3의 배수가 아닙니다.")
# odd(15)
# odd(9)
# odd(20)

# def comp(): #더 큰 수를 리턴
#     x = int(input("정수1 입력 : "))
#     y = int(input("정수2 입력 : "))
#     if x > y:
#         return x
#     else:
#         return y
# print(comp())

# def abs(): #절대 값 입력값x, 리턴X
#     num = int(input("정수 입력 : "))
#     if num >= 0:
#         print("절대값", num)
#     else:
#         print("절대값", -num)
# abs()

# def change_name(): #.find()
#     Name = input("이름 전체 입력 : ")
#     index = Name.find(" ")
#     Frist_name = Name[:index]
#     Last_name = Name[index:]
#     return Last_name + " " + Frist_name
# name = change_name()
# print(name)

# result = []
# for i in range(5):
#     numlist = int(input("정수 입력 : "))
#     if numlist >= 5:
#         result.append(numlist)
#     else:
#         pass
# print(result)

def ListCheck(List):
    List = list(List)
    Resultlist = []
    for i in List:
        if i >= 5:
            Resultlist.append(i)
        return Resultlist
List = [1,2,3,4,5,6,7,8,9,10,12]
print(ListCheck(List))

# def sum():
#     result = num1 + num2
#     print(result)

# def sub():
#     result = num1 - num2
#     print(result)

# def mul():
#     result = num1 * num2
#     print(result)

# def div():
#     result = num1 / num2
#     print(result)

# while True:
#     num1 = int(input("정수1 입력 : "))
#     num2 = int(input("정수2 입력 : "))
#     sel_num = int(input(
#     """계산할 방식을 선택하세요 : 
#     1. 더하기
#     2. 빼기
#     3. 곱하기
#     4. 나누기
#     0. 끝내기
#     """))
#     if sel_num == 1:
#         sum()
#     elif sel_num == 2:
#         sub()
#     elif sel_num == 3:
#         mul()
#     elif sel_num == 4:
#         div()
#     else:
#         break
