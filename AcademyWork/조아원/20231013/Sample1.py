# 복권
# 1. 6개의 숫자
# 2. 1부터 45까지의 랜덤한 숫자가 나와요(단 중복되는 숫자X)

'''
6개의 숫자를 아원학생이 입력해서 랜덤으로 나오는 6개의 중복되지 않는
숫자랑 비교해 몇개를 맞는지 출력하세요.
'''

import random as rd # 라이브러리 불러옴

inputNum = set() # 사용자가 입력할 값을 보관할 장소
# len() = 배열의 길이를 확인할 때 사용!
while(len(inputNum) != 6): # inputNum에 크기가 6이 될 때 까지 반복
    num = int(input("숫자를 입력하세요 : ")) # 계속 입력
    inputNum.add(num) # inputNum에 추가

pcNum = set()

while(len(pcNum) != 6):
    num = rd.randrange(1, 46)
    pcNum.add(num)

check = 0 # 비교해주는 변수!!!

check = pcNum & inputNum # 교집합 함수!
print(f"사용자 입력 : {inputNum}") 
print(f"컴퓨터 입력 : {pcNum}")
if(len(check) == 0):
    print(f"중복된 숫자가 없습니다.")
else :
    print(f"중복된 숫자 : {check}")

if(len(check) == 6):
    print("1등")
elif(len(check) == 5):
    print("2등")
elif(len(check) == 4):
    print("3등")
else :
    print("꽝")