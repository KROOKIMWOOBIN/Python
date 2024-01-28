'''
두 자연수 A와 B가 있을 때, A % B는 A를 B로 나눈 나머지 이다.
예를 들어, 7, 14, 27, 38을 3으로
나눈 나머지는 1, 2, 0, 2이다.
수 10개를 입력받은 뒤, 이를 N으로 나눈 나머지를 구한다.
그 다음 서로 다른 값이 몇 개 있는지
출력하는 프로그램을 작성하세요.
'''
import random as rd

numbers = []

for i in range(10) :
    number = rd.randint(1, 10)
    numbers.append(number)

print(numbers)

n = int(input("숫자를 입력하세요 : "))

after_numbers = []

for i in range(len(numbers)) :
    after_numbers.append(numbers[i] % n)

print(after_numbers)

after_numbers2 = list(set(after_numbers))

print(len(after_numbers2))