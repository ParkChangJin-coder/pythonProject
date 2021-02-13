fruit = ["사과", "사과", "바나나", "복숭아", "포도", "배", "복숭아", "딸기", "키위", "복숭아"]

d = {}

for i in fruit:
    if i in d:  #key가 d라는 딕셔너리에 들어있는가
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
print(d.values())
print(d.keys())


