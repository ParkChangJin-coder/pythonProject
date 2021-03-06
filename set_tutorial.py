# s1 = set([1,2,3])
# s2 = set(["Hello", "Python"])
# s3 = set(["Hello","Hello"]) #중복된 데이터를 저장할 수 없다.
# print(s1)
# print(s2)
# print(s3)
# #print(s1[1]) 집합은 데이터의 순서가 없기 때문에 바로 인덱싱 불가
# s1 = list(s1)
# print(s1[1]) #set를 리스트로 변환

# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print(s1 & s2)#교집합
# print(s1.intersection(s2))
# print(s1|s2)#합집합
# print(s1.union(s2))
# print(s1 - s2) #차집합
# print(s2 - s1)
# print(s1.difference(s2))
# print(s2.difference(s1))
# s1.add(12)
# print(s1)
# s1.update([13,14,15])
# print(s1)
# s1.remove(15)
# print(s1)
# s1.clear() # 전체 삭제
# print(s1)

# a = set([1,2,3,4,5,6])
# b = set([4,5,6,7,8,9])
# c = set([5,6,7,8,9,10])

# print(tuple(a & b & c)) #교집합
# print(tuple(a | b | c)) #합집합
# print(tuple(a - b - c)) #차집합
# print("")
# a = [1,1,5,5,4,3,6,7,2,1,5,5,8,5]
# list_1 = list(set(a))
# print(list_1)

d = set([1,2,3,4,5,6])
e = set([4,5,6,7,8,9])
f = set([5,6,7,8,9,10])
d.remove(1)
d.remove(2)
d.remove(6)
e.remove(4)
e.remove(5)
f.remove(5)
print("")
print(d - e - f)

