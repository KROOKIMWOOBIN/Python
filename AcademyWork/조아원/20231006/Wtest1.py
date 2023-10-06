# 조건문 예제
# 1. 조건문을 사용하여 동물을 입력 받아 등록해 놓은 동물을 찾을 수 있게 해보세요.

#point = input("동물을 입력하세요(예시 : 고양이, 강아지) : ")

#if(point == "고양이"):
#    print("고양이를 찾았습니다.")
#elif(point == "강아지"):
#    print("강아지를 찾았습니다.")



# 반복문 예제
# 1. 반복문을 사용하여 사용자가 원할 때 까지 입력을 돌릴 수 있게 만드세요.

check = 1
while(check):
    point = input("동물을 입력하세요(예시 : 고양이, 강아지) : ")
    if(point == "고양이"):
        print("고양이를 찾았습니다.")
        check = 0
    elif(point == "강아지"):
        print("강아지를 찾았습니다.")
        check = 0
    else:
        print("다시 입력해주세요")

# 함수 예제
# 1. 함수를 사용하여 모듈화를 시키세요.
def petFinder():
    check = 1
    while(check):
        point = input("동물을 입력하세요(예시 : 고양이, 강아지) : ")
        if(point == "고양이"):
            print("고양이를 찾았습니다.")
            check = 0
        elif(point == "강아지"):
            print("강아지를 찾았습니다.")
            check = 0
        else:
            print("다시 입력해주세요")