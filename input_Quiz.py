This_year = int(input("올해의 연도 4자리 : "))
Birth_year = int(input("태어난 연도 4자리 : "))
age = This_year - Birth_year + 1
print("당신의 연령은 : ",  age, " 살 입니다")

Max_Weight = 600
Object1 = float(input("첫 번째 물건의 무게(kg) : "))
Object2 = float(input("두 번째 물건의 무게(kg) : "))
Current_Weight = Max_Weight - (Object1 + Object2)
#Max_Weight -= Object1 + Object2
print("현재 엘리베이터의 허용 무게는 ", Current_Weight," kg입니다." )

Current_Height = float(input("현재 당신의 키 : "))
Man_Standard_Weight = round((Current_Height - 100) * 0.9,2)
print(Man_Standard_Weight)
Woman_Standard_Weight = round((Current_Height - 105) * 0.9,2)
print(Woman_Standard_Weight)
print("현재 당신의 키는  : ", Current_Height, "Cm")
print("당신으 표준 체중은 남성 : ", Man_Standard_Weight, "kg, 여성 : ", Woman_Standard_Weight,"kg 입니다.")