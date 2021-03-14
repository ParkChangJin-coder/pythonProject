#1번문제
address = "부산광역시 진구 부전동"
si = address[:5]
goo = address[6:8]
dong = address[-3:]
print("시 : ",si,", 구 : ",goo,", 동 : ",dong)
#2번문제
say = "I love Pusan"
say = say[:-5] + "B" +  say[-4:]
print(say)
#3번문제
money = "부산 112 2014 9018 01입금 = 10억원"
Bank = money[:2]
Gejoua = money[3:19]
Won = money[-4:]
print("은행 : ",Bank,", 계좌번호 : ",Gejoua,", 금액 : ",Won)
a = "1 + 1 = 3"
b = "1011111101101 -> 23,137"
c = "파이썬은 저급언어이며 컴파일러방식이다."
d = "파이썬은 프로그래밍 언어 중 어려운 편에 속한다."
a = a[:-1] + "2"
b = b[:-6] + "6,125"
c = c[:5] + "고" + c[6:]
d = d[:-11] + "쉬" + d[-9:]
print(a)
print(b)
print(c)
print(d)