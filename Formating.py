print("현재 통장의 잔고는 %d 억원 입니다."%17)
print("현재 통장의 잔고는 %d 억원 입니다."%23)
print("현재 통장의 잔고는 %d 억원 입니다."%55)

print("I eat %d cakes"%3) #정수
print("I eat %s cakes"%"four") #문자열 %s는 모든 자료형을 저장 가능 그 외에는 안됨
print("I eat %f cakes"%3.5) #소수점수
print("I eat %x cakes"%0xad) #16진수

num = 4
print("I eat %d cakes"%num)
print("i ate %s cakes"%"three")
print("i ate %s cakes"%3)
print("i ate %s cakes"%2.55)

print("I ate %d %s cakes"%(3, "three")) #다수 포멧팅
print("")
print("%10s %5s"%("아이유","25")) #10, 5 는 스페이스
print("%10s %5s"%("강도원","40"))
print("")
a = 3.14159265
print("%.2f"%a) #소수점 자르기
print("%10.2f"%a)

print("")
print("Hello %s, Bye %s"%("빡창", "빡창"))
print("Hello {0}, Bye {0}".format("빡창"))
print("{0} {1} {2} {1} {2} {1} {0} {1} {1} {1}".format("빡", "창", "양아치"))
print("")
print(""" I eat {count} cakes
so i sick for {day} days""".format(count=10, day=3))
print("") #format에 앞부분은 숫자로 지정된 포멧팅으로 사용해야 한다.
print(""" I eat {0} cakes
so i sick for {day} days""".format(5, day=4))

kg = "ITBANK"
address = "부산 광역시 수영구 민락동"
start = 12
name = "송진우"
end = 15
height = 192.123456
age = 29
phone = "010-5567-1430"

print("{0} {1} {0}".format(("☆"*7), kg))
print("파이썬 강의 : {start} 시 ~ {end} 시".format(start = start, end = end))
print("본인 이름 : {name}".format(name = name))
print("본인 나이 : {age}".format(age = age))
print("핸드폰 : {phone}".format(phone = phone))
print("주소 : {address}".format(address = address))
print("키 : %.2f"%height)
print("☆☆☆☆☆☆☆☆☆☆%s☆☆☆☆☆☆☆☆☆☆"%kg)
print("")
print("""
☆☆☆☆☆☆☆☆☆☆{title}☆☆☆☆☆☆☆☆☆☆
파이썬 강의 : {start} 시 ~ {end} 시
본인 이름 : {name}
본인 나이 : {age}
핸드폰 : {phone}
주소 : {address}
키 : {height}
☆☆☆☆☆☆☆☆☆☆{title}☆☆☆☆☆☆☆☆☆☆
""".format(start = start, end = end, name = name, age = age, address = address, height = round(height,2), title = kg, phone = phone))

kor,eng,mat = map(int,input("국어, 영어, 수학 점수 입력 : ").split())
sum = kor + eng + mat
avg = float(sum) / 3.0
print("합계 %d 평균 : %.2f"%(sum, avg))