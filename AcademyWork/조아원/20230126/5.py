'''
예제 입력1 
3 ABC
예제 출력1
AAABBBCCC

예제 입력2
5 /HTP
예제 출력2
/////HHHHHTTTTTPPPPP
'''
n = int(input("숫자 입력 : "))
a = input("문자 입력 : ")

for i in a : # forEach문
    for _ in range(n) : # n번만큼 출력
        print(i, end="")
