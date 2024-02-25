'''
1. 사용자로부터 숫자 1개를 입력 받아 그 수의 모든 약수를 출력하세요. 20분까지 혼자 도전!!! 그 이후에 저랑 같이 도전!!!
user = int(input("숫자 1개를 입력 : "))
for i in range(1, user + 1) :
    if user % i == 0 :
        print(i, end=" ")
'''
'''
2. 사용자로부터 숫자 1개를 입력 받아 그 수보다 작은 약수가 아닌 모든 수를 더해서 출력하세요
user = int(input("숫자 1개를 입력 : "))

sum = 0

for i in range(1, user + 1) :
    if user % i != 0 :
        sum = sum + i

print(sum)
'''