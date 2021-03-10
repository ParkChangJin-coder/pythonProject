# kor = int(input("국어점수 입력하세요 : "))
# eng = int(input("영어점수 임력하세요 : "))
# math = int(input("수학 점수를 입력하세요 : "))

# score = (kor + eng + math) / 3

# if score >= 90 and score <= 100:
#     grade = 'A'
# elif score >=80 and score <=89:
#     grade = 'B'
# elif score >=70 and score <=79:
#     grade = 'C'
# elif score >=60 and score <=69:
#     grade = 'D'
# elif score >=0 and score <=59:
#     grade = 'F'
# print("평균 : ",score," ",grade,"입니다")

# result_Aud = input("투표해 주세요")
# A_result = result_Aud.upper().count("A")
# B_result = result_Aud.upper().count("B")
# if A_result > B_result:
#     F_result = A_result
# else:
#     F_result = B_result
# print("A:",A_result,"B:",B_result)
# print("우승자는 ",F_result," 입니다.")

# Count = input("입력 : ")
# ACount = Count.count("A") + Count.count("a")
# BCount = Count.count("B") + Count.count("b")
# print("A는 {0}표, B는 {1}표".format(ACount,BCount))
# if ACount > BCount:
#     print("우승자는 A입니다.")
# elif ACount < BCount:
#     print("우승자는 B입니다.")
# else:
#     print("무승부입니다.")

# count = int(input("만두 개수를 입력하세요 : "))
# amount = count * 1000
# if count <= 10:
#     amount = amount * 0.85
# elif count >= 100:
#     amount = amount * 0.75
#     print(amount)
# cash = amount * 0.9
# print("가격 : ", amount , "현금가 : ", cash)

# ManduCount = int(input("만두개수를 입력하세요 : "))
# Price = ManduCount * 1000
# if ManduCount >= 100:
#     Price *= 0.75
# elif ManduCount >= 10:
#     Price *= 0.85
# print("가격 : {0}원, 현금가 : {1}원".format(Price, Price*0.9))

# birth = str(input("생년월일 6자리 : "))
# gender = int(input("주민번호 뒷자리 첫글자 : "))
# this_year = 2021
# if gender == 1 or gender == 2:
#     year = '19' + birth[:2]
# elif gender == 3 or gender == 4:
#     year = '20' + birth[:2]
# age = (this_year - int(year))+1
# print("성별 정보가 ", gender, " 이므로,", year," 년생",age," 살 입니다")

# BirthNumber = input("생년월일 6자리 : ") #881227 1 의 형식으로 입력
# Birth = BirthNumber[:-2]
# genderNumber = BirthNumber[-1]
# print("생년월일 : ",Birth)
# print("성별 : ",genderNumber)
# if genderNumber == 1 or genderNumber == 2:
#     birthYear = '19' + BirthNumber[:2]
# elif genderNumber == 3 or genderNumber == 4:
#     birthYear = '20' + BirthNumber[:2]
# print("성별 정보가 {0}이므로, {1}년생, {2}년생 입니다.".format(genderNumber,birthYear, 2021 - int(birthYear)))



# parking_time = int(input("주차 시간을 입력하세요 : "))
# amount = 1000
# if parking_time <= 30:
#     pass
# elif parking_time > 30:
#     minute_time = parking_time // 10
#     print(minute_time)
#     amount = (minute_time * 500) + amount 
# print("주차요금은 : ", amount, "원 입니다.")

Minute = int(input("주차시간 입력 : "))
Price = 1000
if Minute > 30:
    Minute -= 30
    Price += (Minute // 10 * 500)
    if Minute % 10 != 0:
        Price += 500
print("주차요금은 : ",Price)

# Minute = int(input("주차한 시간을 입력하세요 : "))

# Price = 1000
# if Minute > 30:
#     Minute -= 30
#     Price +=(Minute // 10 * 500)
#     if Minute % 10 != 0:
#         Price += 500

# print("주차요금은 {0}원입니다.".format(Price))