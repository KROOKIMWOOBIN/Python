'''
사용자로부터 10개의 숫자를 입력받아
모든 수를 다 더해주는 프로그램을 만드세요

입력 예시
5
7
8
9
2

출력 예시
31
'''

'''
사용자로부터 숫자 1개를 입력 받아
그 숫자만큼 반복하여 숫자를 입력하여
다 더해주는 프로그램을 작성하세요

입력 : 3
--------
입력 : 4
입력 : 7
입력 : 11
--------
출력 : 22
'''

'''
--- 숙제 ---
사용자로부터 숫자 1개를 입력받아
그 숫자만큼 반복하여 모든 수를 계속 곱하여
그 결과를 출력하세요
'''

n = int(input("입력 : "))

num = 1

for _ in range(n) :
    a = int(input("입력 : "))
    num = num * a
    print(f"출력 : {num}")