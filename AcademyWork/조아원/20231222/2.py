'''
아원학생이 뱅크 시스템을 만들어보십다. 은행에 입금 출금이 가능하도록 + 잔고 확인까지
'''

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원이 입금되었습니다.")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")
        else:
            print("잔고가 부족합니다.")
    
    def check_balance(self):
        print(f"잔고는 {self.balance}원입니다.")

user1 = BankAccount()

user1.deposit(50000)

user1.withdraw(10000)

user1.check_balance()