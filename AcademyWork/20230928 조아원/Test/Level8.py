# 양의 정수 N 입력 받기
N = int(input("양의 정수 N을 입력하세요: "))

# 소수를 저장할 리스트 생성
prime_numbers = []

# 2부터 N까지의 숫자 중 소수인지 검사
for num in range(2, N + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

# 결과 출력
print(f"2부터 {N}까지의 소수 리스트: {prime_numbers}")