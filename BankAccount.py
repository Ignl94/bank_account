import random


def account_gen():
    account = ""
    total = 0
    while True:
        account += random.randint(0, 9)
        total += 1
        if total == 8:
            return account


class BankAccount:
    routing_number = 109991919
    balance = 0
    account_number = account_gen()

    def __init__(self, full_name):
        self.name = full_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: {amount}")

    def get_balance(self):
        balance = self.balance
        print(f"Your balance is {balance}")
