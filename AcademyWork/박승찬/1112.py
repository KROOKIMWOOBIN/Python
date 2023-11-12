# 함수 사용

# 함수란 모듈화 100~1000줄

# 1. 매개변수가 없는 함수
'''
def printf() :
    print("출력")

printf()
'''
# 2. 매개변수가 있는 함수
'''
def sum(a, b):
    print(a + b)

sum(10, 50)
'''

'''
def sum(a, b):
    return a + b

c = sum(10, 50)

print(c)
'''
'''
def gugudan(num):
    for i in range(1, num + 1) :
        for j in range(1, 10) :
            print(f"{i} * {j} = {i * j}")

gugudan(10)
'''
'''
def trueAndFalse(string):
    if string == "박승찬":
        print("진실입니다.")
    else :
        print("거짓입니다.")

trueAndFalse("박승찬")
'''
'''
def trueAndFalse():
    string = input("이름을 입력해주세요 >>> ")
    if string == "박승찬":
        print("진실입니다.")
    else :
        print("거짓입니다.")

trueAndFalse()
'''

'''
def miniGame() :
    gameEnd = True
    pc = 50
    while gameEnd :
        user = int(input("숫자를 입력해주세요 >>> "))
        if user > pc :
            print("이보다 더 작은 수 입니다.")
        elif pc == user :
            print("맞췄습니다!!!")
            gameEnd = False
        else :
            print("이보다 더 큰 수 입니다.")

miniGame()
'''
