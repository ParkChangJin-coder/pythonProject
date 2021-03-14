List =[]
while True:
    i = int(input("정수 입력: "))
    if i == 0:
        break
    List.append(i)
for v in List:
    print(v,end=" ")
print("Sum = ",sum(List))