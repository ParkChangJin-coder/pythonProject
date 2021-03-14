a = "happy"
#count : 특정 단어의 갯수를 반환
print("a.count('p') : ",a.count('p'))
print("a.count('b') : ",a.count('b'))

a = "Python is best choice"
#find : 특정 단어를 찾아서 가장 먼저 찾아지는 단어의 시작 인덱스 번호 반환
#만약 찾는 단어가 없는경우 -1을 반환한다.
print("a.find('b') : ",a.find("b"))
print("a.find('t') : ",a.find("t"))
print("a.find('k') : ",a.find("k"))
#join : 특정 단어를 단어 사이에 추가하는 기능
print(",".join("abcd"))

a = "hi!"
#upper : 단어들을 전부 대문자로 변환하는 기능
print(a.upper())

a = "HI!"
#lower : 단어들을 전부 소문자로 변환하는 기능
print(a.lower())

a = "   Hello   "
#lstrip : 왼쪽 공백 제거
print(a.lstrip())
a = "   Hello   "
#rstrip : 오른쪽 공백 제거
print(a.rstrip())
a = "   Hello   "
#strip : 양쪽 공백 제거
print(a.strip())

a = "Life is too short"
#replace : 특정 단어를 교체
print(a.replace("Life","My Leg"))

a = "Life is too short"
#split : 특정 단어를 기준으로 문자열을 나누는 기능
print(a.split())
b = a.split()
print("/".join(b))
a = "010 2888 2985"
print("-".join(a.split()))
c = "-".join(a.split())
print(c.split("-"))


a = "Life is too short"
#startswith : 시작 단어가 맞는지 확인하는 기능(True,False)
print(a.startswith("Life"))
print(a.startswith("Lifa"))
#endswith : 끝 단어가 맞는지 확인하는 기능(True,False)
print(a.endswith("short"))
print(a.endswith("shortt"))

a = "life is too short"
#capitalize : 첫 단어만 대문자로 전환
print(a.capitalize())

a = "you need python"
#center(30) : 30칸의 공간을 잡아두고 그안에 문자열을 중앙정렬 후 출력
#ljust(30) : 30칸의 공간을 잡아두고 그안에 문자열을 왼쪽정렬 후 출력
#rjust(30) : 30칸의 공간을 잡아두고 그안에 문자열을 오른쪽정렬 후 출력
print(a.center(30))
print(a.ljust(30))
print(a.rjust(30))