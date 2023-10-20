import random as rd

def game() :
    while(True):
        pc = rd.randrange(1, 4)
        while(True):
            user = input("가위 바위 보 >>> ")
            if(user == "가위" or user == "바위" or user == "보") :
                break
            print("정상적으로 입력이 되지 않았습니다.")
        if pc == 1 :
            pc = "가위"
        elif pc == 2 :
            pc = "바위"
        else :
            pc = "보"
            print(f"유저 : {user} PC : {pc}")
        if(user == pc):
            print("비겻습니다.")
        elif((user == "가위" and pc == "보") or (user == "바위" and pc == "가위") or (user == "보" and pc == "바위")):
            print("이겼습니다.")
            break
        else :
            print("패배했습니다.")
            break




'''
1. 변수 a = 5, b = 10
2. 포맷을 써서 print하세요! f
'''

'''
while문을 사용해서 구구단 9단부터 1단까지 거꾸로 출력
'''

'''
문제 설명
정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ num_list의 길이 ≤ 100
0 ≤ num_list의 원소 ≤ 1,000

입출력 예
num_list	        result
[1, 2, 3, 4, 5]	    [2, 3]
[1, 3, 5, 7]	    [0, 4]
입출력 예 설명
입출력 예 #1

[1, 2, 3, 4, 5]에는 짝수가 2, 4로 두 개, 홀수가 1, 3, 5로 세 개 있습니다.
입출력 예 #2

[1, 3, 5, 7]에는 짝수가 없고 홀수가 네 개 있습니다.
'''

