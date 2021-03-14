print("현재 통장의 잔고는 %d억원 입니다." % 17)
print("현재 통장의 잔고는 %d억원 입니다." % 100)
print("현재 통장의 잔고는 %d억원 입니다." % 23)

print("I eat %d cakes"%3)
print("I eat %s cakes"%"two")
print("I eat %f cakes"%3.5)
print("I eat %x cakes"%0xad)

num = 4
print("I eat %d cakes"%num)
#%s는 모든 자료형을 저장 가능하며 
#%s를 제외한 다른 서식문자는 자료형을 꼭 일치해야 한다
#print("I eat %d cakes"%"two")
print("I eat %s cakes"%2)

print("I eat %d %s"%(3,"cakes"))

print("%10s %5s"%("Name","age"))
print("="*15)
print("%10s %5s"%("아이유","25"))
print("%10s %5s"%("강동원","40"))
print("%10s %5s"%("여진구","24"))

a = 3.14159265
print("%.2f"%a)
print("%10.2f"%a)

print("Hello %s,Bye %s"%("최정호","최정호"))
print("Hello {0},Bye {0}".format("최정호"))
print("{0} {1} {2} {0} {2} {1} {1} {2}".format("최","정호","안녕"))

print("""I eat {count} cakes
so I was sick for {day} days""".format(count=10,day=3))

#format에 앞부분은 숫자로 지정된 포멧팅으로 사용해야한다.
print("""I eat {0} cakes
so I was sick for {day} days""".format(5,day=3))
#print("""I eat {0} cakes
#so I was sick for {day} days""".format(day=3,5))