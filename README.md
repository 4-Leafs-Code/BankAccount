# BankAccount
Just some basic bank accounting codes I helped a friend with

Implement a class named BankAccount. Every bank account has a starting balance of $0.00. The class should implement methods to accept deposits, return the current balance, transfer money from one account to another, and make withdrawals, but an exception should be raised if a withdrawal is attempted for more money than is currently in the account. Create the following methods:

__init__(self, label)	- Creates an instance of BankAccount, setting the balance to $0, with an account name = label
deposit(self, amount)	- Deposits money. Print error message if amount is less than zero
withdraw(self, amount)	- Withdraws money. Print error message iif the amount exceeds the balance
balance(self)	- Returns the amount of money in the account
transfer(self, amount, ID)	- Transfers money between two accounts.   This is essentially a withdraw() against self and a deposit() to ID
__str__(self)
Returns the account name as a string
In the main module, create two accounts one account called checking and one account called savings. Perform the following transactions on both accounts:

Create a variable called cash
Print the starting balance for both accounts and cash
Deposit     $500 into the checking account
Deposit     $100 into the savings account
Transfer    $150 from checking to savings
Deposit     $-50 into checking
Withdraw  $600 from checking
Withdraw  $250 from checking to cash
Withdraw  $100 from savings to cash
Transfer     $ 75 from savings to checking
Print the ending balance of both accounts and cash after each transaction.   An example of the expected output:


-------------------------------------------------------------------------------------------------------------------------------------------------


For Program 12 you will extend the BankAccount() class from Program 10.    We will now model two different types of accounts.  
 A Checking account is a type of BankAccount with additional information about it:   the last used check number, and an amount limit for any single check.  We can also print a check – this (a) increments the check number by 1; (b) reduces the balance by the amount requested, (c) outputs “Check #nnnn for $yy.yy  printed” where #nnnn is the check number and $yy.yy is the amount.    This method should print an error message if the check amount results in an overdraw.  When an account is created the last used check number will be 0000 (stored as a number).

 A Savings account is another type of BankAccount.   It has an interest rate;    we can get the interest rate through an accessor method.  We can also accrue interest by multiplying the current balance by the interest rate times the number of periods provided.

 Specific requirements:

 Use inheritance to define Checking() and Savings() as sub-classes of BankAccount()

For each sub-class
Define the __init__ constructor method which creates the sub-class specific instance variables and uses the parent __init__ constructor method to label the account and set the initial balance
Define the other methods necessary to support the actions described.
Create a main() program which
Creates an instance of a checking account with the label “My Checking”; the limit for any check will be $250 dollars
Creates an instance of a savings account with the label “My Savings”; the interest rate will be 0.05  (aka 5%)
Perform the following transactions:
Deposit $100 to “My Checking
Deposit $50 to “My Savings”
Print a check for $50 (should output "Check 0001 for $50.00 printed")
Display the balance for checking (should be $50)
Accrue 2 months of interest  (period would equal 2/12 as a float)  in savings
Print savings balance (should be $50.42)
Print a check for $10 (should output "Check 0002 for $10.00 printed")
Display the checking account balance (should be $40)
Print a check for $250 (should print an error that the amount is higher than available balance)
Deposit $2000 to checking
Print a check for $1000 (should print an error that the amount is higher than limit)
Print the checking & savings balances
