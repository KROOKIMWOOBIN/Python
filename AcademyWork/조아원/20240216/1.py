import random

# 9x9 배열 생성
array = [[0 for col in range(9)] for row in range(9)]

# 1부터 100까지의 숫자를 리스트로 생성
numbers = list(range(1, 101))

# 배열에 랜덤한 수 채우기
for row in range(9):
    for col in range(9):
        num = random.sample(numbers, 1)[0]  # numbers 리스트에서 랜덤한 하나의 숫자 선택
        array[row][col] = num
        numbers.remove(num)  # 선택된 숫자는 numbers 리스트에서 제거

# 전체 배열 출력
for row in array:
    for num in row:
        print(f'{num:3}', end=' ')  # 공간을 3칸으로 맞추어 출력
    print()

# 가장 큰 값과 위치 찾기
max_value = -1
max_row = -1
max_col = -1

for row in range(len(array)):
    for col in range(len(array[row])):
        if array[row][col] > max_value:
            max_value = array[row][col]
            max_row = row 
            max_col = col  

# 가장 큰 값과 위치 출력
print(f'가장 큰 값: {max_value}')
print(f'위치: ({max_row + 1}, {max_col + 1})')  
