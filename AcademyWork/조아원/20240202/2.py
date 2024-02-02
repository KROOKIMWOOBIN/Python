'''
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지
알아내는 프로그램을 작성하세요.
단, 대문자와 소문자를 구분하지 않는다.
--- 예시 ---
aaazz a
basda a
basbc b
--- Hint ---
upper()
lower()
'''

user = input("입력하세요 : ")
user = user.upper()

count_list = {}

for count in user :
    if count in count_list :
        count_list[count] += 1
    else :
        count_list[count] = 1

max_count = 0
check_word = ''

for word, count in count_list.items() :
    if count > max_count :
        max_count = count
        check_word = word

print(check_word)