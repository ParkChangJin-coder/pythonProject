# num = int(input("정수 입력 : "))
# if num % 2 != 0:
#     pass #아무런 동작을 하지 않는다
# else:
#     print("짝수 입니다")


# num_1 = int(input("정수 입력 : "))
# if num_1 % 5 == 0:
#     print(num_1)
# else: 
#     print(str(num_1) + "는 5의 배수가 아닙니다")

# num_2 = int(input("정수 입력 : "))
# if num_2 % 2 != 0:
#     print(str(num_2) + " 는 홀수 입니다")
# else:
#     print(str(num_2) + " 는 짝수 입니다")

# num_3, num_4 = map(int,input("정수 2개 입력 : ").split(' '))
# if num_3 % num_4 == 0:
#     print("첫 번재 숫자는 두 번째 숫자의 배수입니다.")
#     print(("{0}은 {1}의 배수 입니다").format(num_3,num_4))
# else: 
#     print("배수가 아닙니다!")

# num_5, num_6 = map(int,input("정수 2개 입력 : ").split(" "))
# if num_5 > num_6 and num_5 % 2 == 0:
#     print(str(num_5) + "가 더 크고 짝수 입니다.")
# elif num_6 > num_5 and num_6 % 2 == 0:
#     print(str(num_6) + "가 더 크고 짝수 입니다.")
# else:
#     print("아무것도 아니네요")

# num_7, num_8 = map(int,input("정수 2개 입력 : ").split(" "))
# Sum78 = num_7 + num_8
# if Sum78 % 2 == 0 and Sum78 % 3 == 0:
#     print(str(Sum78) + "는 짝수이자 3의 배수입니다.")
# else: 
#     print(str(Sum78) + "는 아무것도 아니네요")
# #절대값 = num 일 경우 -num 으로 양수로

# year, month, day = map(int,input("년, 월, 일 입력 : ").split())
# fortune = year - (month + day)
# #fortune = str(fortune)
# if fortune % 10 == 0: #%10은 해당 숫자의 1의 자리를 가져올 수 있다.
#     print("대박!", fortune % 10)
# else:
#     print("그냥저냥", fortune % 10)

# station = int(input("정거장 수 : "))
# if station < 10:
#     print( "총 소요 시간은" + str(station * 2) + " 분 입니다.")
# elif station >= 10:
#     station_time = station * 4
#     if station_time >= 60:
#         hour = station_time // 60
#         minute = station_time % 60
#         print("총 소요 시간은 " + str(hour) + " 시간 "+ str(minute) + " 분 입니다.")
#     else:
#         print( "총 소요 시간은 " + str(station_time) + " 분 입니다.")

# stationCount = int(input("정거장수 : "))
# if stationCount > 10:
#     Countminute = 4
# else:
#     Countminute = 2
# totalMinute = stationCount * Countminute
# print("총 소요 시간은 {0} 시간 {1} 분 입니다.".format(totalMinute//60,totalMinute%60))


MyDic = {"Money":"돈", "Monkey":"원숭이", "Apple":"사과"}
key = input("영단어 입력 : ")
if key in MyDic:
    Value = input("영단어 뜻 입력 : ")
    if Value == MyDic[key]:
        print("정답입니다")
    else:
        print("틀렸습니다.")
else:
    print("해당 단어가 없습니다.")
