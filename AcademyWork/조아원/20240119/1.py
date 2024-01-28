'''
1. 총 N개의 정수가 주어졌을 때, 정수 K가 몇 개인지 
    구하는 프로그램을 작성하시오
조건
1. 숫자의 크기는 1부터 10
'''

import random as rd

numbers = []

n = int(input("n을 입력해주세요 : "))

for _ in range(n) :
    number = rd.randint(1, 10)
    numbers.append(number)

print(numbers)

k = int(input("찾을 숫자를 입력해주세요 : "))

print(numbers.count(k))

'''
35분까지 풀어보기
Hint는 20분에 제공
1. count()
2. for()
'''
