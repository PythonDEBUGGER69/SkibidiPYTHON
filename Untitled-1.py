
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name 

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):