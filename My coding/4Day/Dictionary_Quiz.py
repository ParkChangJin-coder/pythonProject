mart = {"다이제":1000,"메로나":500,"코카콜라":700,"츄파츕스":500}
print(mart)
menu = tuple(mart.keys())
print(menu)

price = sum(tuple(mart.values()))
print("Price : ",price)

key = input("메뉴 입력 : ")
value = int(input("가격 입력 : "))
mart[key] = value

key = input("메뉴 입력 : ")
value = int(input("가격 입력 : "))
mart[key] = value

print(mart)