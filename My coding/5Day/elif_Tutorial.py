money = int(input("소지하고있는 금액 입력 : "))
if money >= 50000:#5만원 이상
    print("소고기 먹으러 가자!")
elif money >= 30000: # 5만원 미만에서 3만원 이상
    print("돼지고기 먹으러 가자!")
elif money >= 10000: # 3만원 미만에서 1만원 이상
    print("돈까스 먹으러가자")
else:
    print("굶어야지...")