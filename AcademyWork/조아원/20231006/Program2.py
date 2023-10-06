class Calcul:
    def __init__(self, num1, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)
    
    def sum(self):
        print(self.num1 + self.num2)

    def sub(self):
        print(self.num1 - self.num2)

    def numCh1(self, num1): # 10
        self.num1 = num1 # 5 = 4
    
    def printf(self):
        print(f"{self.num1} 와 {self.num2}")

    
end = 1 # 끝낼건지 종료 여부 확인

while(end):
    start = int(input("1. 계산기 생성 2. 종료 >>> "))
    end2 = 1 # 계산기 동작 여부
    if(start == 1):
        num1 = int(input("첫번 째 숫자를 입력해주세요 : "))
        num2 = int(input("두번 째 숫자를 입력해주세요 : "))
        cal = Calcul(num1, num2)
        while(end2):
            check = int(input("1. 더하기 2. 빼기 3. 숫자변경 4. 종료 >>> "))
            if(check == 1): 
                cal.sum()
            elif(check == 2):
                cal.sub()
            elif(check == 3):
                chNum = int(input("변경할 숫자를 선택하세요 1, 2 >>>"))
                if(chNum == 1):
                    chNum1 = int(input("변경할 숫자 입력 >>> "))
                    cal.numCh1(chNum1)
                    print(f"{chNum1}로 변경 완료")
            elif(check == 4):
                print("계산기 종료")
                end2 = 0
            else:
                print("다시 입력해주세요...")
    elif(start == 2):
        print("프로그램을 종료합니다.")
        end = 0
    else:
        print("다시 입력해주세요...")
