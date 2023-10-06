# 숫자 입력
number = int((input("숫자를 입력하세요 : ")))
# 모든 수를 더 할 변수 선언
sum = 0
# 반복문 돌려서 1부터 number까지 더하기
for i in range(1, number + 1) :
    sum = sum + i
# 결과 출력
print(sum)