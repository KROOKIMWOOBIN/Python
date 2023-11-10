import random

class MiniGame :
    def __init__(self):
        self.value = 0
    def selectGame(self):
        while(True) :
            print("0. 게임 종료")
            print("1. 가위 바위 보")
            print("2. 숫자 맞추기")
            choice = int(input("어떤 게임을 하시겠습니까? >>> "))
            if choice == 0:
                break
            elif choice == 1 :
                self.rockPaperScissors()
            elif choice == 2:
                self.guessNumber()
            else :
                print("올바른 게임을 선택해주세요")
    def rockPaperScissors(self):
        gameEnd = True
        while(gameEnd) :
            user1 = input("USER1 가위 바위 보 >>>")
            user2 = input("USER2 가위 바위 보 >>>")
            print(f"USER1 = {user1} USER2 = {user2}")
            if((user1 == "가위" and user2 == "보") or (user1 == "바위" and user2 == "가위") or (user1 == "보" and user2 == "바위")) :
                print("USER1가 이겼습니다.")
                gameEnd = False
            elif(user1 == user2) :
                print("비겼습니다.")
            else :
                print("USER2가 이겼습니다.")
                gameEnd = False
    def guessNumber(self):
        target_number = random.randrange(1, 101)
        guess = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
        if guess == target_number:
            print("정답입니다!")
        elif guess < target_number:
            print("더 큰 수를 입력해보세요.")
        else:
            print("더 작은 수를 입력해보세요.")
                

game1 = MiniGame()
game1.selectGame()