"""
1번문제
Movie = ["어벤져스","레슬러","챔피언","얼리맨","당갈","콰이어트 플레이스"]
print(Movie)
print("4위 영화 {0}".format(Movie[3]))
print(Movie[:2])# 1 ~ 2 위
print(Movie[3:-1])# 4 ~ 5 위
Tmp = Movie[:2] + Movie[3:-1]
print(Tmp)

2번문제
a = [3,5,2,6,1,4]
a.sort()#오름차순
a.reverse()#역순
print(a)
b = [input(),input(),input(),input()]
c = b;
print(c)
"""

a = [3,5,2,6,1,4]
print("7을 추가하기 전 평균 : %.1f"%(sum(a)/len(a)))
a.append(7)
print("7을 추가한 후 평균 : %.1f"%(sum(a)/len(a)))