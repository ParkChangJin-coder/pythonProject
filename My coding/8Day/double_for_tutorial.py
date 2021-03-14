#학년이 총 1 ~ 3까지 있으며 각 학년당 반이 12개반이 있다.

for Class in range(1,4):#학년에 해당하는 반복문
    print("{0}{1}학년{0}".format("="*8,Class))
    for num in range(1,13):#반에 해당하는 반복문
        print("{0}학년 {1}반".format(Class,num))

print("구구단")
for i in range(2,10):
    print("====={0}단=====".format(i))
    for j in range(1,10):
        print("{0} x {1} = {2}".format(i,j,i*j))