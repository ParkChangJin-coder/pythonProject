# name = input("이름입력:")
# age = input("나이입력:")
# print("이름은 : ",name," 나이는 : ",age, " 살이다")


# LastName = input("성을 입력 하세요 : ")
# FirstName = input("이름을 입력 하세요 : ")
# FullName = LastName + " " + FirstName
# print("My name is : ", FullName)

# num1 = input("첫 번째 정수 입력 : ")
# num2 = input("두 번째 정수 입력 : ")
# print(num1 + num2)

#input은 기본적으로 str로 받는다
# num = 10
# print(type(num))
# fnum = 2.38
# print(type(fnum))
# name = "Park Chang Jin"
# print(type(name))
# status = True
# print(type(status))

# num1 = int(input("정수 입력 : "))
# num2 = int(input("정수 입력2 : "))
# print(num1 + num2)

#한번에 input 받기
# num1, num2, num3 = input("정수 세개 입력 : ").split() #"띄어 쓰기를 기준으로 정보를 분리해서 가져온다"
# print("num1 :",num1, "num2 : ", num2, "num3 :", num3)

#','로 컴마를 기준으로 데이터를 받아온다
# num1, num2, num3 = input("정수 3개 입력 : ").split(',')
# print("num1 :",num1, "num2 : ", num2, "num3 :", num3)
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# print(num1 + num2 + num3)



#float, round
# fnum = float(input("첫 번째 실수 입력 : "))
# fnum2 = float(input("두 번째 실수 입력 : "))
# result = round((fnum + fnum2),2)
# print(result)

# print(int(False))
# print(int(True))
# print(float(True))
# print(float(False))
# print(str(True))
# print(str(False))
# print(bool(True))
# print(bool(False))

#int -> bool
# print(bool(-17))
# print(bool(0))
#int -> float
# print(float(17))
# print(float(0))
#float -> int
# print(int(0.17))
# print(int(10.5))
#str -> bool 문자열에 문자가 있으면 True 없으면 False
# print(bool("Hello"))
# print(bool(""))
# round
print(round(2.335,2))

#map을 써서 여러개의 정보를 int로 바꾸고 콤마를 기준으로 데이터 받기
# num1, num2, num3 = map(int,input("정수 3개 입력 : ").split(','))
# print("num1 :",num1, "num2 : ", num2, "num3 :", num3)
# print(num1 + num2 + num3)

# width = input("가로(mm) : ")
# length = input("세로(mm) : ")
# height = input("높이(mm) : ")
# To_meter = float(0.001) int 가 아닌 float
# weight = input("무게(kg) : ")
# cbm = ((int(width) * To_meter) * (int(length) * To_meter) * (int(height) * To_meter))
# 
# print("cbm 값은 : ", cbm, " 입니다")
