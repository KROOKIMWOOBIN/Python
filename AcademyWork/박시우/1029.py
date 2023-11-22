'''
b라는 변수를 만들고
10을 넣어 출력해보세요
변수 b랑 그냥 알파벳b를 같이 출력해보세요
'''

'''
b = 10
# 1번 방식
print("{} b".format(b))
# 2번 방식
print(f"{b} b")
'''

# for while
# 구구단
'''
num1 = 5
num2 = 10

print(num1 * num2)
'''
'''
# 반복문으로 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
'''

for i in range(1, 6) :
    print(i * 2)