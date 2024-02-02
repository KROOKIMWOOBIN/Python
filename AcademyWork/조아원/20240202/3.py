'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 
각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 
출력하는 프로그램을 작성하시오.

40분까지 ㅎㅇㅌ!!! 40분 되면 알려드릴게요!!!
'''

count = 0 # 그룹 단어 개수

# 단어 개수 입력
n = int(input("단어의 개수를 입력하세요 : "))

for _ in range(n) :
    word = input("단어를 입력하세요 : ")

    be_char = ''
    char_set = set()

    is_word = True
    for char in word :
        if char != be_char and char in char_set :
            is_word = False
            break

        char_set.add(char)
        be_char = char

    if is_word :
        count += 1

print(count)
