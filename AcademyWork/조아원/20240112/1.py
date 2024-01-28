'''
문제설명
문자열 binomial이 매개변수로 주어집니다. 
binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, 
op는 '+', '-', '*' 중 하나입니다. 
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.
'''
'''
제한사항
0 ≤ a, b ≤ 40,000
0을 제외하고 a, b는 0으로 시작하지 않습니다.
'''
'''
입출력 예
binomial	    result
"43 + 12"	    55
"0 - 7777"	    -7777
"40000 * 40000"	1600000000
'''
'''
# 1번 방법
def solution(binomial):
    a, op, b = binomial.split()
    a = int(a)
    b = int(b)
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    return answer
# 2번 방법
def solution(binomial):
    answer = eval(binomial)
    return answer
    '''
'''
split() - 문자열을 매개변수의 따라 나눈다.
사용방법
string = "a b c"
a, b, c = split(string)
a = "a"
b = "b"
c = "c"
int()
eval()
'''
'''
문제 설명
문자열 str이 주어집니다.
문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str의 길이 ≤ 10

입출력 예
입력 #1
abcde

출력 #1
a
b
c
d
e
'''

'''
str = input()
for i in range(len(str)) :
    print(str[i])
    '''
