'''
1. 단어S와 정수 n이 주어졌을 때,
S의 n번째 글자를 출력하는 프로그램을 작성하세요.
--- Hint ---
1. 인덱싱
S = "단어"
n = 숫자
print(S[n-1])
2. 문자열 슬라이싱
S = "단어"
n = 숫자
print(S[n-1:n])
'''
s = input("단어를 입력해주세요 : ")
check = True
while(check) :
    n = int(input("정수 1개를 입력해주세요 : "))
    if len(s) + 1 > n :
        check = False
print(s[n-1])

