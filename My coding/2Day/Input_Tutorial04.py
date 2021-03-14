#name = input("이름 입력 : ")
#age = input("나이 입력 : ")
#print("이름 : ",name,"\t나이 : ",age)
#LastName = input("성을 입력하세요 : ")
#FirstName = input("이름을 입력하세요 : ")
#FullName = LastName + FirstName
#print("제 이름은 ",FullName," 입니다.")
#print(FullName*10)

#num1 = input("첫 번째 정수 입력 : ")
#num2 = input("두 번째 정수 입력 : ")
#print 안에선 무조건 문자로 정보를 모두 인식을한다.
#print(num1 + num2)
"""
num = 10
print("num Type : ",type(num))
fnum = 2.38
print("fnum Type : ",type(fnum))
name = "최정호"
print("name Type : ",type(name))
#True(참) , False(거짓)
status = True
print("status Type : ",type(status))
"""
#input은 기본적으로 입력받은 값은 str자료형(문자)로 인식한다.
#num = input("정수 입력 : ") #문자입력
#num2 = input("정수 입력 : ")
#print("합계 : ",int(num) + int(num2))
#num = int(input("정수입력 : "))#형변환
#num2 = int(input("정수입력 : "))
#print(num + num2)

#input().split() : 띄어쓰기를 기준으로 정보를 분리해서 가져온다
#num,num2,num3 = input("정수 3개 입력").split()
#print("num = ",num,"\tnum2 = ",num2,"\tnum3 = ",num3)

#input().split(',') : ,를 기준으로 정부를 분리해서 가져온다
#num,num2,num3 = input("정수 3개 입력").split(',')
##print("num = ",num,"\tnum2 = ",num2,"\tnum3 = ",num3)
#print(int(num)+int(num2)+int(num3))

#num,num2,num3 = input("정수 3개 입력").split(',')
#num= int(num)
#num2= int(num2)
#num3 = int(num3)
#print(num+num2+num3)

#map(int,input().split(',')) : ,기준으로 여러개의 정보를 int형으로 입력받는다.
#num,num2,num3 = map(int,input("정수 3개입력").split(','))
#print(num+num2+num3)

#fnum1 = float(input("첫 번째 실수 입력 : "))
#fnum2 = float(input("두 번째 실수 입력 : "))
#print(fnum1," + ",fnum2," = ",fnum1 + fnum2)

#bool -> int
print(int(True))
print(int(False))
#bool -> float
print(float(True))
print(float(False))
#bool -> str
print(str(True))
print(str(False))
#int -> bool
#0은 False 0이 아닌 모든 숫자는 True
print(bool(-17))
print(bool(0))
#int -> float
print(float(17))#17.0
#int -> str
print(str(17))#17
#float -> bool
print(bool(20.13))#True
print(bool(0.00))#False
#float -> int
#소숫점 수를 정수로 변환 시 소숫점 뒷자리가 사라진다.
print(int(20.7743))
#float -> str
print(str(15.3432))
#string -> bool
#문자가 있으면 True 없으면 False
print(bool(""))#False
print(bool("Hello"))#True
#string -> int
#문자를 정수로 바꿀 시 문자 내용중 숫자가 아닌 것 이 있으면 안된다.
print(int("30"))
#string -> float
print(float("12.23"))

print(round(4.734))#1의자리까지 반올림하여 출력
print(round(2.34862,2))#2번째 소숫점 자리 까지 반올림하여 출력
