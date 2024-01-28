'''
N의 정수들 중에 가장 큰 값을 찾고
그 값이 몇 번째 Index에
있는 지 같이 출력하세요
'''
import random as rd

numbers = []
n = int(input("정수 개수를 입력하세요 : "))

for i in range(n) :
    number = rd.randint(1, 100)
    numbers.append(number)

print(numbers)

index = 0
max = numbers[0]

for i in range(len(numbers)) :
    if(max < numbers[i]) :
        index = i
        max = numbers[i]

print(f"{index} : {max}")