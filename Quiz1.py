print("Hello, Programming")
print("Hello, python")
print("박창진")

print("백두산  35 살")
print("부활 26 살" )
print("시나위 66 살")

print("""
Hello Python! 
☆\\(^_^)/☆
Python is very easy \'Programming Language\'
i'm 100% sure!
\"Welcome Python World!\"
""")

def singer(name, Age):
    print(name,Age," 살")

singer("백두산 ", 20)
singer("부활 ", 30)
singer("시나위 ", 50)

#리스트에 있는 가수명을 하나씩 집어 넣고, 나이는 1 ~ 100까지 랜덤으로 입력
import random
singerlist = ["백두산", "부활", "시나위"]

#for문으로 작성
for i in range(len(singerlist)):
  age = random.sample(range(1,100),1)  
  print(singerlist[i] +" "+ str(age) + " Years Old")
#while문으로 작성
j = 0
while True:
    age = random.sample(range(1,100),1)
    print(singerlist[j] + " " + str(age) + " 살입니다")
    j += 1
    if j == len(singerlist):
        break
