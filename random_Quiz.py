# import random

# i = 1
# A_score = 100
# B_score = 100
# time = int(input("주사위를 몇번 던지겠습니까 : "))
# while i <= time:
#     A_num = random.randint(1,6)
#     B_num = random.randint(1,6)
#     print("A의 주사위 : ",A_num)
#     print("B의 주사위 : ",B_num)
#     print(i,")round",A_num,':',B_num)
#     print("")
#     if A_num > B_num:
#         B_score -= A_num
#     elif A_num < B_num:
#         A_score -= B_num
#     else:
#         pass
#     i += 1
# print("A의 점수는 {0}, B의 점수는 {1}".format(A_score, B_score))

samsung = random.randint(0,2)
lotte = random.randint(0,2)
while 