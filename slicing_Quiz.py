adress = "부산광역시 수영구 민락동"
si = adress[:5]
goo = adress[6:9]
dong = adress[10:]
print("시 : ", si, "구 : ", goo, "동 :", dong)

say = "I love Pusan"
print(say[:6] + " Busan")

money = "부산 112 2014 9018 01 입금 = 10억원"
bank = money[:2]
account = money[3:19]
won = money[25:]
print("은행 : ", bank, "계좌 : ", account, "금액 : ", won)

a = "1 + 1 = 3"
b = "1011111101101 -> 23,137"
c = "파이썬은 저급언어이며 컴파일러 형식이다"
d = "파이썬은 프로그래밍 언어중에 어려운 편에 속한다"

print("a = ", a[:7], "2")
print("b = ", "0b101101001100001", b[13:])
print("c = ", c[:5], "고급", c[7:])
print("d = ", d[:16], "쉬운", d[19:])




