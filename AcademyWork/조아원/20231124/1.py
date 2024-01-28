import random
user_name = ""  # 유저 이름
user_move = ""  # 유저의 선택
computer_move = 0  # 컴퓨터의 선택
computer_score = 0  # 컴퓨터의 점수
user_score = 0  # 유저의 점수
play_again = ""  # 다시 플레이할지 여부
play = True  # 게임 진행 여부
user_win = 0  # 유저의 승리 횟수
computer_win = 0  # 컴퓨터의 승리 횟수
game_moves = ["ROCK", "SCISSORS", "PAPER"]  # 가위바위보 선택지
count = 1  # 라운드 카운트

user_name = str(input("이름을 입력하세요: "))  # 유저 이름 입력
print("안녕하세요", user_name, "님, 가위 바위 보 게임을 시작합니다!")
# ---------------------------------------------------------

while play == True:  # 게임 진행 중일 동안 반복
    user_move = (str(input("가위, 바위, 보 중 하나를 선택하세요: ")))  # 유저가 가위, 바위, 보 중 하나 선택
    user_move = user_move.upper()  # 입력을 대문자로 변환하여 통일

    # 컴퓨터가 랜덤하게 가위, 바위, 보 중 하나 선택
    computer_move = game_moves[random.randrange(0, 3)]

    print(f"유저: {user_move}, 컴퓨터: {computer_move}")

    if user_move == computer_move:  # 유저와 컴퓨터가 같은 선택을 했을 때
        print("비겼습니다.")
    elif user_move == "ROCK" and computer_move == "SCISSORS":  # 유저가 바위, 컴퓨터가 가위인 경우
        print("유저가 이겼습니다!")
        user_score = user_score + 1
    elif user_move == "SCISSORS" and computer_move == "PAPER":  # 유저가 가위, 컴퓨터가 보인 경우
        print("유저가 이겼습니다!")
        user_score = user_score + 1
    elif user_move == "PAPER" and computer_move == "ROCK":  # 유저가 보, 컴퓨터가 바위인 경우
        print("유저가 이겼습니다!")
        user_score = user_score + 1
    else:  # 그 외의 경우는 컴퓨터가 이긴 경우
        print("컴퓨터가 이겼습니다!")
        computer_score = computer_score + 1

    if count == 5:  # 5라운드가 끝났을 때
        if user_score > computer_score:  # 유저의 점수가 컴퓨터의 점수보다 높으면
            print("유저가 라운드에서 이겼습니다!")
        elif user_score < computer_score:  # 유저의 점수가 컴퓨터의 점수보다 낮으면
            print("컴퓨터가 라운드에서 이겼습니다!")

        play_again = input("다시 플레이하시겠습니까? (y/n): ")

        if play_again == "y":  # 다시 플레이할 경우
            if user_score > computer_score:  # 유저의 점수가 컴퓨터의 점수보다 높으면
                user_win = user_win + 1  # 유저의 승리 횟수 증가
            elif user_score < computer_score:  # 유저의 점수가 컴퓨터의 점수보다 낮으면
                computer_win = computer_win + 1  # 컴퓨터의 승리 횟수 증가
            user_score = 0
            computer_score = 0
            count = 0  # 라운드 카운트 초기화

        elif play_again == "n":  # 다시 플레이하지 않을 경우
            play = False  # 게임 종료
            print(f"유저: {user_win} 승, 컴퓨터: {computer_win} 승")
            if user_score > computer_score:  # 유저의 점수가 컴퓨터의 점수보다 높으면
                print("유저가 최종 승리했습니다!")
            elif user_score < computer_score:  # 유저의 점수가 컴퓨터의 점수보다 낮으면
                print("컴퓨터가 최종 승리했습니다!")
            else:  # 무승부인 경우
                print("무승부입니다!")
    count = count + 1  # 라운드 카운트 증가
