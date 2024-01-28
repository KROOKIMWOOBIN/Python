'''
정수 N개로 이루어진 배열에서 K보다 작은 모든 수를 출력하세요
조건
1. 숫자의 크기는 1부터 10까지
'''
import random as rd

numbers = []
n = int(input("정수 개수를 입력하세요 : "))

for i in range(n) :
    number = rd.randint(1, 10)
    numbers.append(number)

print(numbers)

k = int(input("숫자를 입력하세요 : "))

for i in range(len(numbers)) :
    if numbers[i] < k :
        print(numbers[i], end=" ")