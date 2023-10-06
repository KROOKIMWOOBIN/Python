# 조건문 예제
# 1. 조건문을 사용하여 동물을 입력 받아 등록해 놓은 동물을 찾을 수 있게 해보세요.

#point = input("동물을 입력하세요(예시 : 고양이, 강아지) : ") <-
#print("고양이를 찾았습니다.") <-

# 반복문 예제
# 1. 반복문을 사용하여 사용자가 원할 때 까지 입력을 돌릴 수 있게 만드세요.


# true = 1 false = 0 
# 반복문에 a라는 변수에 1이 들어가면 돌아가고 0이 들어가면 멈춤
# 메소드
'''
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

petFinder()
'''

# 붕어빵 틀
class PetFinder:
    def __init__(self, age, name):
        self.age = int(age)
        self.name = name
    
    def printf(self):
        print(f"동물의 이름은 {self.name}이고 나이는 {self.age}입니다.")

    def year(self):
        print(f"동물의 이름은 {self.name}이고 나이는 {self.age + 1}입니다.")
    

# 클래스는 항상 첫 단어가 대문자, 변수와 함수는 소문자로 시작

# 붕어빵
dog = PetFinder("4", "강아지")
dog.printf()

cat = PetFinder("2", "고양이")
cat.printf()

cat.year()
        