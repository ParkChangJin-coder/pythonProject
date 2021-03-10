import random

#randint : 시작 숫자부터 끝 숫자 사이에 임의 숫자
print(random.randint(1,100))
#random : 0 ~ 1 사이의 임의 플롯
print("random.random() : ", random.random())
#uniform(시작 소숫점, 끝 소숫점) : 시작 소숫점 ~ 끝 소숫점 사이의 임의 플롯
print("random.uniform() : ", random.uniform(0.1,0.02))
#randrange(정수) : 0부터 정수 미만의 수 사이에서 임의수
#randrange(시작숫자, 끝숫자)
print("random.randrange() : ", random.randrange(10))
print("random.randrange() : ", random.randrange(5,8))
#randrange(시작, 끝, 숫자간격) : 시작 부터 끝 미만 사이에서 숫자 간격만큼
#떨어진 수 들 중 임의 수를 뽑아준다
print("random.randrange() : ", random.randrange(1,101,2)) #1부터 2씩 증가한 수 중에 랜덤
#choice(list) : list, tuple, dictionary, set 등등 데이터 구조에서 랜덤으로 하나 가져옴
list = [1,2,3,4,5,6,7,8,9,10]
print("choice() : ", random.choice(list))
#sample : list, tuple, dictionary, set 등등 데이터 구조에서 랜덤으로 특정 개수만큼 들고옴
print("sample() : ", random.sample(list, 3))
#shuffle : list, tuple, dictionary, set 등등 데이터 구조에서 랜덤으로 섞음
random.shuffle(list)
print("shuffle() : ", list)
