# 양의 정수 N 입력 받기
N = int(input("양의 정수 N을 입력하세요: "))

# 피보나치 수열 초기값 설정
fibonacci_sequence = [1, 1]

# N개의 피보나치 수열 생성
if N <= 0:
    print("양의 정수를 입력해주세요.")
elif N == 1:
    print("피보나치 수열:", [1])
elif N == 2:
    print("피보나치 수열:", fibonacci_sequence)
else:
    for i in range(2, N):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    # 결과 출력
    print("피보나치 수열:", fibonacci_sequence)