print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*5)
print(3*(2+1))

print('풍선')
print("나비")
print("ㅋ"*9)

#boolean 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + " 의 이름은 " + name + " 예요")
# hobby = "공놀이"
#print("연탄이는 " + str(age) + " 살이며, " + hobby + " 을 아주 좋아해요")
print(name, "는 ", age, " 살이며, ", hobby, " 을 아주 좋아해요")

print("연탄이는 어른일까요? " + str(is_adult))

#Quiz 변수명 : station 변수값 "사당", "신도림", "인천공함" 순서대로 입력
#출력 문장 : xx행 열차가 들어오고 있습니다.


def train(station):
     print(station, " 행 열차가 들어오고 있습니다.")

train("사당")
train("신도림")
train("인천공항")

print(2**3)
print(5%3) #나머지
print(5//3) #몫
print(10 > 3) #True
print(4 >= 7) #False
print(3 == 3)
print( 1 != 3)
print(not (1 != 3))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))
print(5 > 4 > 3)
print(5 > 4 > 7)

print(2 + 3 * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)

number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 3
print(number)

print(abs(-5))
print(pow(4, 2))
print(max(12, 5))
print(min(12, 5))
print(round(3.14))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16)) #4의 제곱근

from random import *
print(random()) #0.0 ~ 1.0 임의의 값
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1) #1 ~ 10

print(int(random() * 45) + 1)
#randrange(1, 46)

for i in range(6):
 print(str(randrange(1, 46)) + " lotto") # 1~ 45 미만의 임의의 값 생성

for j in range(3):
 print("오프라인 스터디 모임 날짜는 " + str(randrange(4, 28)) + "일로 선정되었습니다.")

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 " + str(date) + "일로 선정되었습니다.")

for k in range(3):
     date2 = randint(1, 28)
     print("모임은" + str(date2) + "일 입니다.")








