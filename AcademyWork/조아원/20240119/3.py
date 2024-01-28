'''
N개의 정수가 주어질 때
가장 작은 값과 가장 큰 값을 구하는 프로그램을 제작
출력 예시
7 35
'''
import random as rd

numbers = []
n = int(input("정수 개수를 입력하세요 : "))

for i in range(n) :
    number = rd.randint(1, 100)
    numbers.append(number)

print(numbers)

print(f"{min(numbers)} {max(numbers)}")