'''
랜덤한 9x9 2차원 배열을 생성하여
1~9까지에 랜덤한 수를 채워 사용자로부터 1~9까지의 수 중 1개의 값을 입력받아
9x9 표를 만들어 해당하는 숫자는 그대로 아닌 수는 0으로 출력하는 프로그램을 작성하세요
'''

import random
'''
[random.randint(1, 9) for _ in range(9)] 이 과정만 있는 경우 1~9까지의 랜덤한 수를 담은 1차원 배열을 생성하지만
[[random.randint(1, 9) for _ in range(9)] for _ in range(9)] 이 과정으로 인해 9번 반복하여 2차원 배열을 생성한다.
'''
array = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]

num = int(input("숫자를 1개 입력해주세요 >>> "))

for col in array :
    for row in col :
        if row == num :
            print('{:2}'.format(row), end='')
        else :
            print('{:2}'.format(0), end='')
    print()