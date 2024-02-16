'''
소수 찾기 

주어진 N개의 랜덤한 수 중 소수가 몇 개인지 찾아 출력하는 프로그램을 작성하세요
'''

def is_prime(num):
    """
    주어진 숫자가 소수인지 판별하는 함수입니다.
    소수인 경우 True를 반환하고, 소수가 아닌 경우 False를 반환합니다.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1): 
       if num % i == 0:
            return False
    return True

def find_primes(numbers):
    """
    주어진 리스트에서 소수를 찾아 정렬하여 반환하는 함수입니다.
    """
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    primes.sort()  # 소수를 정렬
    return primes

# 테스트
import random

N = int(input("랜덤한 수의 개수를 입력하세요: "))
numbers = [random.randint(1, 1000) for _ in range(N)]

print("랜덤한 수:", numbers)
print("소수:", find_primes(numbers))
