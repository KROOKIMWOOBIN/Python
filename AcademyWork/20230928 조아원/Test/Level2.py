# 양의 정수 입력 받기
n = int(input("양의 정수를 입력하세요: "))

# 초기값 설정
factorial = 1

# 팩토리얼 계산
if n < 0:
    print("음수는 팩토리얼을 계산할 수 없습니다.")
elif n == 0:
    print("0의 팩토리얼은 1입니다.")
else:
    for i in range(1, n + 1):
        factorial *= i

    # 결과 출력
    print(f"{n}의 팩토리얼은 {factorial}입니다.")

















def factorial(n):
    # 초기값 설정
    fac = 1

    # 팩토리얼 계산
    if n < 0:
        print("음수는 팩토리얼을 계산할 수 없습니다.")
    elif n == 0:
        print("0의 팩토리얼은 1입니다.")
    else:
        for i in range(1, n + 1):
            fac *= i

        # 결과 출력
        print(f"{n}의 팩토리얼은 {fac}입니다.")
        
