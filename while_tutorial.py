import os #System 함수를 사용하기 위해 가져온 기능

# num = 0
# while True:
#     os.system("cls") #화면에 print된 문자를 전부 지워주는 역할
#     print("""
#     ===========menu==========
#     1. 정수입력
#     2. 입력된 정수 출력
#     3. 종료
#     """
#     )
#     select = int(input("메뉴 선택 : "))
#     if select == 1:
#         num = int(input("정수 입력 : "))
#     elif select == 2:
#         print("입력된 정수 : ", num)
#         os.system("pause")
#     elif select == 3:
#         exit(0) 



# num = 0

# while num <= 9:
#     print("num = {0}".format(num))
#     num += 1

# Count = 1

# while Count <= 21:
#     print("드라마 {0}회 시청".format(Count))
#     Count += 1
# print("드라마 결말을 보았습니다.")

# print("열 번 찍어 안 넘어 가는 나무 없다")
# hit = 0
# while hit <= 10:
#     print("나무를 {0}번 찍었습니다.".format(hit))
#     hit += 1
# print("나무가 넘어 갔습니다.")

# Monster_HP = 1000
# Turn = 1

# while Monster_HP > 0:
#     print("=========={0}턴==========".format(Turn))
#     print("몬스터 체력 : ", Monster_HP)
#     print("1.기본공격 2.스킬공격")
#     Attack = int(input("선택 : "))
#     if Attack == 1:
#         print("몬스터에게 300의 데미지")
#         Monster_HP -= 300
#     elif Attack == 2:
#         print("몬스터에게 500의 데미지")
#         Monster_HP -= 500
#     else:
#         print("잘못 입력 하셨습니다.")
#     Turn += 1
#     os.system("pause")
# print("Monster is defeated!")