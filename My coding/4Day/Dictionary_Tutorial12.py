#Dictionary 생성
Info = {"Name":"최정호","Phone":"010-2888-2985","Birth":"0618"}
print(Info)
print("이름 : ",Info["Name"])
print("전화번호 : ",Info["Phone"])
print("생일 : ",Info["Birth"])

#Dictionary 데이터 추가
Info["성별"] = "남자"
print(Info)
print("성별 : ",Info["성별"])
#Dictionary 데이터 삭제
del Info["Phone"]
#Dictionary 데이터 수정
print(Info)
Info["성별"] = "여자"
print(Info)

Info_Key = Info.keys()
print(Info_Key)
Info_Key = list(Info.keys())
print(Info_Key)
print(Info_Key[1])
print(Info[Info_Key[1]])
Info_Key = tuple(Info.keys())
print(Info_Key)
#Info Dictionary 안에 성별 키가 있는지 확인
print("성별" in Info)
print("Phone" in Info)

#Info Dictionary 안에 성별 키가 없는지 확인
print("성별" not in Info)
print("Phone" not in Info)

#clear : 전체 삭제
Info.clear()
print(Info)