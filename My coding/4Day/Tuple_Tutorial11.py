#Tuple : 초기값으로 데이터를 지정하며
#그 후 데이터 수정 삭제 추가 불가능하다.
kim = ("A형","황인","남자")
print(kim)
print(kim[1])#index로 값 접근 가능
#kim[0] = 'B형' #오류
#print(kim)
#del kim[0] #오류
print(kim[:1])#슬라이싱 가능
a = (1,2,3)
b = (4,5,6)
print(a + b)#덧셈 가능
print(a * 3)#곱셈 가능
c = [7,8,9]
#print(a + b + c)#Tuple 은 같은 Tuple 끼리만 연산이 가능

