# info = {"name" : "빡창","성별" : "남성", "생년월일" : "19881227" }
# print(info)
# print(info["name"])
# print(info["성별"])
# print(info["생년월일"])
# info["전화번호"] = "2706"
# print(info)
# print(info["전화번호"])
# del info["전화번호"]
# print(info)
# print("")
# info_key = info.keys() #키 만 저장
# print(info_key)
# info_key = list(info_key) # list(info.keys())
# print(info_key)
# print(info_key[1])
# print(info[info_key[1]])
# info_key = tuple(info.keys())
# print(info_key)
# print("성별" in info) #info 딕셔너리 안에 존재 하는가
# print("번호" in info) #False
# print("번호" not in info) #True 없는지 확인

# info.clear() #전체 삭제
# print(info)


mart = {"다이제" : 1000, "메로나" : 500, "콜라":700, "추파춥스":500}
info_menu = tuple(mart.keys())
print(info_menu)
info_Sum_Price = sum(mart.values())
print(info_Sum_Price)
# key_add1 = input()
# value_add1 = input()
# mart[key_add1] = value_add1
# key_add2 = input()
# value_add2 = input()
# mart[key_add2] = value_add2

for i in range(2):
   key_add = input()
   value_add = input()
   mart[key_add] = value_add

print(mart)
