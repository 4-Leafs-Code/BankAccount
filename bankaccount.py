class BankAccount(object):
    def __init__(self, label):
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
        self.last = 0
        self.limit = 0
        super().__init__( "My Checking")

    def last_check(self):
        if self.last == 1000:
            self.last = ""
        return "{0:0>4}".format(self.last)

    def print_check(self,amount):
        if amount > self.limit:
            print("Error: amount exceeds account limit")
        elif amount > self.balance:
            print("Error: amount exceeds account balance")
        else:
            self.withdraw(amount)
            self.last += 1
            amount = '{:04.2f}'.format(amount)
            print("Check #" + self.last_check(), "for $" + amount, " printed")


class Savings(BankAccount):
    def __init__(self):
        self.rate = 0
        super().__init__("My Savings")

    def accure(self, period):
        self.balance += self.balance * self.rate * period
        return self.balance
