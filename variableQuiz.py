birth = 881227
age = 34
kor = 84
eng = 77
mat = 80
score_list = [kor, eng, mat]

print("생년월일 :", birth)
print("내 나이는 ", age, "살 입니다.")
print("국어 ", kor, "점, ", "영어 ", eng, "점, ", "수학 ", mat, "점")
#print("국어 ", kor, "점, 영어", eng, "점, 수학", mat, "점")
print("합계 : ", sum(score_list))
print("평균 : ", round(sum(score_list) / len(score_list), 1))

height = 178.4
weight = 87.5
print("나의 키는 ", height, "cm 이며, 나의 몸무게는 " , weight, "kg 입니다.")

station = 11
min = 37 
print("한 역을 지나치는데 걸리는 시간은 : ", min / station )