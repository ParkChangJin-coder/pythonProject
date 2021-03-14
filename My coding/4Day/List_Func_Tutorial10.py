a = [1,2,3]
print(a)
a[2:] = [3,4]
print(a)
#append : 마지막 위치에 데이터 추가 하는 기능
a.append(5)
print(a)
a.append([6,7])
print(a)

#sort : 오름차순 정렬
a = [4,8,2,7,6]
print(a)
a.sort()
print(a)

a = ['i','t','b','a','n','k']
print(a)
a.sort()
print(a)

a = [4,8,2,7,6]
a.sort()
#reverse : 데이터의 순서를 역행
a.reverse()
print(a)

#index : 특정 데이터의 index번호를 반환
print(a.index(6))
#print(a.index(10))

#insert(추가될 index,추가할 값) : 원하는 위치에 데이터를 추가
a = [1,2,3]
print(a)
a.insert(0,4)
print(a)
a.insert(3,5)
print(a)

#remove : 특정 데이터를 하나 삭제하는 기능
a = [1,2,3,1,2,3]
print(a)
a.remove(3)
print(a)
a.remove(3)
print(a)

#pop : 가장 마지막에 있는 데이터를 삭제 후 빼온다.
a = [1,2,3]
print(a)
print(a.pop())
print(a)

#pop(index번호) : 특정 index위치에 있는 데이터를 꺼낸다.
a = [1,2,3]
print(a)
print(a.pop(1))
print(a)

#append 로 list를 추가할 경우 중첩list로 저장된다.
a = [1,2,3]
print(a)
a.append([4,5])
print(a)

#extend : list 확장하여 다른 list 정보를 추가한다.
#list 간에 +와 동일한 결과를 가질 수 있다. 
a = [1,2,3]
print(a)
a.extend([4,5])
print(a)
a += [6,7]
print(a)

#count : list 안에 특정 데이터의 개수를 반환한다.
a = [1,2,3,1]
print(a.count(1))
#len : list의 전체 개수를 반환한다.
print(len(a))