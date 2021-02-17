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