# apart = [[101,102,103,104],[201,202,203,204],[301,302,303,304]]
# k=1
# for i in apart:
#     #print(i)
#     for j in i:
#         print(j, "호 부착완료")
#     print("{0}층에 모두 부착완료".format(k))
#     k += 1

# num = int(input("출력할 별의 행 입력 : "))
# for y in range(num):
#     for x in (y+1):
#         print("*",end="")
#     print()

# num = int(input("출력할 별의 행 입력 : "))
# for y in range(num):
#     for j in range(num-y-1):
#         print(" ",end="")
#     for j in range(y+1):
#         print("*",end="")
#     print()

# num = int(input("출력할 별의 행 입력 : "))
# for y in range(num):
#     for j in range(num - y- 1):
#         print(" ",end="")
#     print("*" * (y * 2 + 1))

num = int(input("출력할 별의 행 입력 : "))
for y in range(num):
    for x in range(y+1):
        print(" ",end="")
    for x in range((num - y - 1) * 2 + 1):
        print(y,end="")
    print()
