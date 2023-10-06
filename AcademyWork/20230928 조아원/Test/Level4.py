# 양의 정수 입력 받기
num = int(input("양의 정수를 입력하세요: "))

# 1과 자기 자신을 제외한 다른 약수가 있는지 확인
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# 결과 출력
if is_prime:
    print(f"{num}은(는) 소수입니다.")
else:
    print(f"{num}은(는) 소수가 아닙니다.")
