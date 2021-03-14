"""
1번문제
kg = "KG ITBANK"
address = "부산광역시 부산진구 부전동"
start = 2
name = "최정호"
end = 7
height = 180.21433241
age = 31
phone = "010-2888-2985"
print("{0}{1}{0}".format(("☆"*7),kg))
print("파이썬 강의 : {Start}시 ~ {End}시".format(Start = start,End = end))
print("본인 이름 : %s"%name)
print("본인 나이 : %d"%age)
print("핸드폰 : %s"%phone)
print("주소 : %s"%address)
print("키 : %.2f"%height)
print("{0}{1}{0}".format(("☆"*7),kg))

kor,eng,mat = map(int,input("국어,영어,수학 점수 입력 : ").split())
sum = kor + eng + mat
avg = float(sum) / 3.0
print("합계 : %d 평균 : %.2f"%(sum,avg))

num1,num2 = map(int,input("정수 2개 입력 : ").split())
print("거듭 제곱 : {0} 나누었을 때 몫 : {1} 나머지 {2}".format(num1**num2,num1//num2,num1 % num2))
"""

StationMin = 3
StationCount = int(input("역 개수 입력 : "))
TotalMin = StationMin * StationCount
print("총 소요시간 %d"%TotalMin)