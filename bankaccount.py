class BankAccount():
    def __init__(self,label):
        self.name = label
        self.balance = 0

    def deposit(self,amount):
        if amount < 0:
            print("Error: Deposit amount must be positive")
        else:
            self.balance += amount
            return self.balance

    def withdraw(self,amount):
        if amount < 0:
            print("Error: Withdraw amount must be positive")
        elif amount > self.balance:
            print("Error: Insufficient funds")
        else:
            self.balance -= amount
            return self.balance

    def balance(self):
        return self.balance

    def transfer(self, amount, ID):
        if amount < 0:
            print("Error: Transfer amount must be positive")
        elif amount > self.balance:
            print("Error: Insufficient funds")
        else:
            self.balance -= amount
            ID.balance += amount
            return self.balance, ID.balance

    def __str__(self):
        return("{} account: {}".format(self.name, self.balance))

class Checking(BankAccount):
    def __init__(self):
        self.last_check = 0000
        self.check_limit = 0
        self.print_check = False


    def check(self):
        pass
