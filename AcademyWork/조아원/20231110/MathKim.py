class MathKim :
    def __init__(self, num) :
        self.num = num
    def sum(self, num) :
        self.num += num
        return self.num
    def sub(self, num) :
        self.num -= num
        return self.num
    def fibo (self) :
        result = []
        a, b = 1, 1
        for i in range(self.num):
            result.append(a)
            a, b = b, a + b
        print(result[-1])
        
    


