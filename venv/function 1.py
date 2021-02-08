#먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕"
# 나이가 10살 에서 20살 사이면 "안녕하세요"
# 그 외에는 "안녕하십니까"

def sayhello(name, age):
    if age < 10:
        print(name + ", 안녕")
    elif age >= 10 and age <= 20:
        print(name + ", 안녕하세요")
    else:
        print(name +", 안녕하십니까")

sayhello("철수", 5)
sayhello("영희", 15)
sayhello("빡창", 34)