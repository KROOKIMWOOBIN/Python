'''
1. 반복문을 사용하여 10개의 숫자를 입력받아
    모든 수를 다 더하세요
'''
sum = 0

for i in range(1, 10 + 1) :
    num = int(input("숫자 입력 >>> "))
    sum = sum + num

print(sum)
