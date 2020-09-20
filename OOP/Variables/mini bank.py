class customer:
    """ This program will perform deposit and withdraw option of a bank application"""
    bankName = 'City Bank'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Current balance is::', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Sorry!! You have insufficient funds to withdraw')
        else:
            self.balance = self.balance - amount
            print('After the withdraw the current balance is::', self.balance)


print('Welcome to', customer.bankName)
name = input('Please enter your name:: ')
customerObject = customer(name)
while True:
    print('please choose from the following option:\n d--deposit\n w-- withdraw \n e-- e-exit')
    option = input('Please enter your option::  ')
    if option.lower() == 'd':
        amount = float(input('Enter the amount to deposit::  '))
        customerObject.deposit(amount)

    elif option.lower() == 'w':
        amount = float(input('Enter the amount to withdraw::  '))
        customerObject.withdraw(amount)
    elif option.lower() == 'e':
        print('Thank you for banking:: ')
        break
    else:
        print('Please enter your valid option:: ')
