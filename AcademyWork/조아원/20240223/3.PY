'''
한개의 숫자를 입력받으면 그 숫자의 약수를 모두 출력하세요
'''

num = int(input("숫자 1개를 입력해주세요 : "))
list = []
for i in range(1, num + 1) :
    if num % i == 0 :
        list.append(i)

print(list)