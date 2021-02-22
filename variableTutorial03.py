# '='는 대입연산자. 정보를 저장하는 연산자(명령어)
My_Int_Variable = 30
print(My_Int_Variable + 10)
Age = 20
print("나의 나이는", Age + 1, " 세입니다")
Age = 30
print("나의 나이는", Age, " 세입니다")
Height = 180.34
print("나의 키는 ", Height, " 입니다")

birth = 881227
age = 34
kor = 84
eng = 77
mat = 80
score_list = [kor, eng, mat]

print("생년월일 :", birth)
print("내 나이는 ", age, "살 입니다.")
print("국어 ", kor, "점, ", "영어 ", eng, "점, ", "수학 ", mat, "점")
print("합계 : ", sum(score_list))
print("평균 : ", round(sum(score_list) / len(score_list), 1))
