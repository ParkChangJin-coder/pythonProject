# a = [[10,20],
#      [30,40],
#      [50,60]]

# #print(a[1][0])
# #list [세로 줄수] [가로 줄 수]
# for y in a:
#     for x in y:
#         print(x,end="")
#     print()

i = 1
for y in range(8):
    for x in range(8):
        if i < 10:
            print("0",end="")
        print(i,end=" ")
        i+=1
    print()
