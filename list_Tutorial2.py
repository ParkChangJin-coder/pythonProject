# print("정수 4개 입력")
# a= [input(),input(),input(),input()]
# print("입력값 : :", a)
# print(a[0] + a[2])

# song = [input(),input(),input(),input()]
# kim = [input(),input(),input(),input()]
# Lee = [input(),input(),input(),input()]
# print(song,kim,Lee)


# a = [1,2,3]
# a.append(5) # 데이터 추가
# print(a)
# a.append([6,7,8])
# print(a)
# a.append(9)
# print(a)

# a = [2,8,9,5,6,3,7]
# print(a)
# a.sort()
# print(a)

# a = ['i','t','b','a','n','k']
# print(a)
# a.sort()
# print(a)

# a = [2,8,9,5,6,3,7]
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# print(a.index(5))

# a = [2,8,9,5,6,3,7]
# a.insert(0,4) # 위치, 데이터 삽입
# print(a)

# a = [1,2,3,1,2,3]
# a.remove(3)
# print(a)
# a.remove(3) #특정 값을 삭제 del은 인덱스 번호로 삭제
# print(a)

# a = [1,2,3,1,2,3]
# a.pop() #가장 마지막에 있는 데이터를 빼고 출력
# print(a)
# a.pop(1)
# print(a)

# a = [1,1,2,3]
# a.extend([4,5]) #append 는 중첩 리스트로 데이터 등록 List와 동일하게 더할 수 있다
# print(a)
# b = [6,7]
# a.extend(b)
# print(a)
# print(a.count(1))

# a = [1,2]
# b = [3,4]
# list = a + b
# print(list)
# print(len(list))

movie_List = ["1위:어벤져스", "2위:레슬러", "3위:챔피언", "4위:얼리맨", "5위:당갈", "6위:콰이어트 플레이스"]
#print(movie_List[3])
print("영화 랭킹 {0}".format(movie_List[3]))
a1 = movie_List[:2]
b1 = movie_List[3:5]
new_List = a1 + b1
print(a1)
print(b1)
print(new_List)

# a = [3,5,2,6,1,4]
# a.sort()
# a.reverse()
# print(a)
# b = [input(),input(),input(),input()]
# b = input().split()
# c = b
# print(c)
# print(c.index("Pen"))

# a2 = [3,5,2,6,1,4]
# Avr = sum(a2) / len(a2)
# print("7을 추가하기 전 평균 : ",Avr)
# print(a2)
# a2.append(7)
# Avr7 = sum(a2) / len(a2)
# print(a2)
# print("7을 추가한 후 평균 : ",Avr7)