"""
List =[]
while True:
    i = int(input("정수 입력 : "))
    if i == 0:
        break
    List.append(i)
for v in List:
    print(v,end=" ")
print("Sum = ",sum(List))
"""
Movies = {"라야와 마지막 드래곤":"돈 홀","미나리":"정이삭",
"극장판 귀멸의 칼날: 무한열차":"소토자키 하루오","리스타트":"조 카나한"}

for name in Movies.keys():#영화 이름만 출력
    print(name,end=" ")
print()
for item in Movies.items():#영화명,감독 튜플로 출력
    print(item,end=" ")
print()
for name,director in Movies.items():#영화명,감독이름 따로 출력
    print("영화명 : {0}\t감독이름 : {1}".format(name,director))