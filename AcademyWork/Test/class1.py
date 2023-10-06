class Test :
    def __init__(self, money):
        self.money = money
    
    def sum(self, acount):
        if(acount > 0):
            self.money += acount
            print(f"{self.money}")
        else:
            print("0원은 입금이 안됩니다.")


class Test2 :
    def __init__(self, numA):
        self.numA = numA
    
    def sum(self, numB):
        self.numA += numB
        print(f"{self.numA}")

a = Test2(0)

a.sum(10)

