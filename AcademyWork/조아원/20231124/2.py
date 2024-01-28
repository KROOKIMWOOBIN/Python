'''
for i in range(1, 10):
    for j in range(2, 10):
        print(f"{i} * {j} = {i * j}")
'''

# 1. 한개의 매개변수를 받아서 그 매개변수의 크기까지 1~9 곱하기가 출력

'''
def gugudan(num) :
    for i in range(1, num + 1):
        for j in range(1, 10) :
            print(f"{i} * {j} = {i * j}")

gugudan(25)
'''

# UpDown 게임 숫자 맞추기 30회 안에?

import random

def ud ():
    guess=0
    guess_number=0

    guess_number = random.randrange(0, 100)
    for i in range(30):
        guess=int(input("숫자를 입력해 주세요 >>> "))
        if guess_number>guess:
            print("up")
        elif guess_number<guess:
            print("down")
        elif guess_number==guess:
            print("correct!")
        if i == 0:
            print("failed")

ud()
