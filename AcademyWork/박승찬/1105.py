'''
import random as rd

gameEnd = True
com = rd.randrange(1, 101)
count = 0

while gameEnd :
    count = count + 1
    num = int(input("숫자를 입력해주세요 >>> "))
    if(num == com) :
        print(f"유저 = {num} 컴퓨터 = {com}")
        print(f"{count}회 만에 이겼습니다.")
        gameEnd = False
    elif num > com :
        print(f"{num}보다 더 낮은 수 입니다.")
    elif num < com :
        print(f"{num}보다 높은 수 입니다.")
    else :
        print("다시 한번 입력해주세요.")
'''

player1 = ""
player2 = ""

while (player1 != "가위" and player1 != "바위" and player1 != "보") :
        player1 = input("Player1 가위 바위 보 >>> ") 

while (player2 != "가위" and player2 != "바위" and player2 != "보") :
        player2 = input("Player2 가위 바위 보 >>> ") 

print(f"player1 = {player1} player2 = {player2}")

if((player1 == "가위" and player2 == "보") or 
     (player1 == "바위" and player2 == "가위") or 
     (player1 == "보" and player2 == "바위")):
        print("player1이 이겼습니다.")
elif player1 == player2 :
        print("비겼습니다.")
else :
        print("player2가 이겼습니다.")

        