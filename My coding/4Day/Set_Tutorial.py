#set : 집합으로 데이터를 관리하는 자료구조
#집합은 중복된 데이터를 저장할 수 없다.
#집합은 데이터의 순서가 없어
s1 = set([1,2,3])
print(s1)
s2 = [1,1,2,2,3,3,4,4,5,5,5]
print(s2)
#print(set(s2))
print(list(s1)[1])

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
#교집합 : 두 집합의 공통된 원소집합
#& : 앤퍼센트 or 앤드(And)
print(s1 & s2)
print(s1.intersection(s2))
#합집합 : 두 집합의 전체 원소 집합
#| : 파이프
print(s1 | s2)
print(s1.union(s2))
#차집합 : 두 집합의 교집합을 제외한 나머지
print(s1 - s2)# s1에서 s2와의 교집합을 제외한 나머지
print(s1.difference(s2))
print(s2 - s1)# s2에서 s1과의 교집합을 제외한 나머지
print(s2.difference(s1))

#집합의 데이터 추가
s1.add(7)
print(s1)

#여러 데이터 추가
s1.update([8,9,10])
print(s1)

#특정 데이터 삭제
s1.remove(7)
print(s1)

#전체 삭제
s1.clear()
print(s1)