# 양의 정수 입력 받기
n = int(input("양의 정수를 입력하세요: "))

# 입력한 숫자의 구구단 출력
if n <= 0:
    print("양의 정수를 입력해주세요.")
else:
    print(f"{n}단 출력:")
    for i in range(1, 10):
        result = n * i
        print(f"{n} x {i} = {result}")