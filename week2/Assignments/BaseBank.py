class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, withdrawlAmount):
        if (withdrawlAmount >= self.balance):
            self.balance = self.balance - withdrawlAmount
        else:
            print("Insufficient Balance")
        
    def displayBalance(self):
        print(" Available Balance : ", self.balance)
    
if (__name__ == "__main__"):
    b1 = BankAccount("Mahesh", 1000, "Savings")
    b2 = BankAccount("Siva", 2000, "Current")

    b1.deposit(2000)
    b1.withdraw(3000)
    b1.displayBalance()

    b2.deposit(2000)
    b2.withdraw(3000)
    b2.displayBalance()