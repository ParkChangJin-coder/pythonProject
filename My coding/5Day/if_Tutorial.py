"""
age = int(input("나이 입력 : "))
if age >= 20:
    print("당신은 성인",end=' ')
else:
    print("당신은 미성년자",end=' ')
print("입니다.")

Money = int(input("소지하고 있는 금액 입력 : "))

if Money >= 20000:
    print("치킨을 시켜먹자.")
else:
    print("다음에 시켜먹자...")

num = int(input("정수 입력 : "))
if num < 0:
    print("{0}은 음수 입니다.".format(num))
else:
    print("{0}은 양수 입니다.".format(num))

num = int(input("5 * 7 ? "))
if num == 35:
    print("정답!!!")
else:
    print("오답...")


money = int(input("소지하고있는 금액 입력 : "))
if money >= 50000:#5만원 이상
    print("소고기 먹으러 가자!")
if money < 50000 and money >= 30000: # 5만원 미만에서 3만원 이상
    print("돼지고기 먹으러 가자!")
if money < 30000 and money >= 10000: # 3만원 미만에서 1만원 이상
    print("돈까스 먹으러가자")
if money < 10000 and money >= 0:
    print("굶어야지...")

#남자인지 여자인지 입력과 나이를 입력한 후
#20살 이상의 남자는 군대 입영 대상자
#20살 미만이거나 여자면 군대 입영 비대상자

age = int(input("나이 입력 : "))
gender = input("성별 입력(남/여) : ")

if age >= 20 and gender == "남":
    print("군대 입영 대상자 입니다.")
if age < 20 or gender =="여":
    print("군대 입영 대상자가 아닙니다.")
if not(age >= 20 and gender == "남"):
    print("군대 입영 대상자가 아닙니다.")
"""

print('a' not in ('a','b','c'))#True
print(7 not in [1,2,3,4,5]) #False
print('a' not in "itbank") #True
print('b' not in {1:'a',2:'b',3:'c'})#False
print(2 not in {1:'a',2:'b',3:'c'})#True

pocket = ["스마트폰","지갑","신분증","5만원권"]
if "5만원권" in pocket:
    print("돼지고기 먹으러 가자!")
else:
    print("ATM기로 가자!")

print("="*20)
print("\t짝수 판별!")
print("="*20)

num = int(input("정수 입력 : "))
if num % 2 != 0:
    pass#아무런 동작을 하지 않겠다.
else:
    print("짝수 입니다.")