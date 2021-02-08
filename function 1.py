# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕"
# 나이가 10살 에서 20살 사이면 "안녕하세요"
# 그 외에는 "안녕하십니까"

def sayhello(name, age):
    if age < 10:
        print(name + ", 안녕")
    elif 10 <= age <= 20:
        print(name + ", 안녕하세요")
    else:
        print(name + ", 안녕하십니까")


def sayhello2(name, age, time):
    # 시간별 인사를 time으로 정하기
    if time <= 12:
        time = " 좋은아침"
    elif 12 < time <= 18:
        time = " 점심 식사 하셨어요?"
    else:
        time = " 집에 갑시다"
    # 나이를 받기
    if age < 10:
        print(name + ", 안녕" + time)
    elif 10 <= age <= 20:
        print(name + ", 안녕하세요" + time)
    else:
        print(name + ", 안녕하십니까" + time)


sayhello("철수", 5)
sayhello("영희", 15)
sayhello("빡창", 34)

sayhello2("철수", 5, 10)
sayhello2("영희", 15, 14)
sayhello2("빡창", 34, 19)
