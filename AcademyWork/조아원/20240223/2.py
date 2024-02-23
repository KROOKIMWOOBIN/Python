'''
단어 추측 게임
1. 컴퓨터는 미리 단어 목록에서 하나의 단어를 선택합니다.
2. 사용자는 힌트를 보고 추측한 단어를 입력합니다.
3. 입력한 단어와 컴퓨터가 선택한 단어를 비교하여 결과를 출력합니다.
4. 단어의 글자와 위치가 모두 일치하는 경우는 "정답"으로 표시합니다. 
5. 단어의 글자가 일치하지 않는 경우는 "불일치"로 표시합니다.
6. 사용자가 정답을 맞출 때까지 계속해서 단어를 입력받고 결과를 출력합니다.
7. 정답을 맞추면 축하 메시지와 함께 시도한 횟수를 출력합니다.

예시
단어 추측 게임을 시작합니다!
컴퓨터가 선택한 단어를 추측해보세요.

힌트: 5글자, 첫 번째 글자는 'A', 두 번째 글자는 'P'입니다.

단어를 입력하세요: APPLE
결과: 정답 축하합니다! 정답을 맞추셨습니다. 시도한 횟수: 1
'''
import random

com = ['APPLE', 'BANANA', 'AVOCADO', 'BLUEVERRY', 'CHERRY', 'COCONUT']

gameEnd = False
count = 0
choice = com[random.randint(0, len(com) - 1)]

print("단어 추측 게임을 시작합니다!")
print("컴퓨터가 선택한 단어를 추측해보세요.")

print(f"힌트: {len(choice)}글자, 첫 번째 글자는 '{choice[0]}', 마지막 글자는 '{choice[len(choice) - 1]}'입니다.")

while not gameEnd :
    user = input("단어를 입력하세요: ")
    count = count + 1
    if choice == user.upper() :
        print(f"정답 축하합니다! 정답을 맞추셨습니다. 시도한 횟수: {count}")
        gameEnd = True
    else :
        print("불일치")

