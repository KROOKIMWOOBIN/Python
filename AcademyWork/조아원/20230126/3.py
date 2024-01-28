'''
n개의 숫자가 공백 없이 쓰여있다.
이 숫자를 모두 합해서 출력하는 프로그램
--- 예시1 ---
54321
출력 : 15
--- 예시2 ---
7000000000000000000000000
출력 : 7
'''
'''
a = input("숫자를 입력하세요 > ")
sum = 0
for i in a :
    sum += int(i)
print(sum)
'''
'''
1. for문, foreach문
for문
1 2 3 4 5 6 7 8 9
foreach문
a = abcde
a b c d e
'''
'''
a = "123754"

for i in a :
    if int(i)%2 == 0 :
        print(i)
        '''