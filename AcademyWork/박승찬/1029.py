# if문은 조건문
# while, for

# while <- 변수를 따로 선언

'''
num = 0

while(num < 10):
    print(num)
    num = num + 1
'''

# for <- 내부에서 변수를 선언

'''
for num in range(10):
    print(num)
'''

# if문은 참과 거짓 1 0

'''
a = 1

if(a == 1): 
    print("True")
elif(a == 5):
    print("a = 5")
else :
    print("False")
'''

# 1123131
'''
1241241
123141
1231233
'''

# 가위 바위 보
# 2명의 사람

'''
user1 = input("user1 가위 바위 보 >>> ")
user2 = input("user2 가위 바위 보 >>> ")

print(f"user1 : {user1} user2 : {user2}")

if((user1 == "가위" and user2 == "보") or (user1 == "바위" and user2 == "가위") or (user1 == "보" and user2 == "바위")):
    print("user1가 이겼습니다.")
else:
    print("user2가 이겼습니다.")
'''



# end는 참과 참이 될 때만 참이 된다.
# or는 참과 거짓일 때도 참이 된다.


num1 = int(input("첫번 째 숫자를 입력해주세요 : "))
num2 = int(input("두번 째 숫자를 입력해주세요 : "))

if(num1 > num2):
    print(f"{num1} - {num2} = {num1 - num2}")
else:
    print("큰 수를 먼저 적고 그 다음 작은 숫자를 입력해주세요.")