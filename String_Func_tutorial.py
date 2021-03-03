a = "happy"
print(a.count('p'))#몇개 존재 하는가
print(a.count('b'))

a = "Python is best choise"
print(a.find('b')) #몇 번째에 있는가
print(a.find('t'))
print(a.find('k')) #없는 경우 -1 return
print(a.find("best"))

print(",".join("abcd")) #사이에 넣기

b = "hi"
print(b.upper())#대문자 변환
c = "HI"
print(c.lower())#소문자 변환

d = "   He llo   "
print(d.lstrip()) #왼쪽 공백 삭제
print(d.rstrip()) #오른쪽 공백 삭제
print(d.strip()) #양쪽 공백 삭제

e = "life is too short!"
print(e.replace("short","long")) #특정 문자열 변환
print(e.split())
f = e.split()
print("/".join(f))
g = "010 1234 5678"
print("-".join(g.split())) #스페이스를 - 로 split에 아무 것도 없으면 스페이스 기준으로 나눔
print(g.split("-"))

print(e.startswith("life"))
print(e.startswith("lifa")) #시작 단어가 맞는지 확인하는 기능(True, False)

print(e.endswith("short!"))
print(e.endswith("thort!")) #끝나는 단어가 맞는지 확인하는 기능(True, False)

print(e.capitalize()) #첫 단어만 대문자로 전환
h = "You need Python"
print(h.center(30)) #중앙정렬
print(h.ljust(30)) #왼쪽 정렬
print(h.rjust(30)) #오른쪽 정렬

