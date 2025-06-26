class BankAccounT:
    def check_balance(self):
        print("Taking ur money")

class balance(BankAccounT):
    def __init__(self, balance):
        self.balance = balance
    def realbalance(self):
        print("Your balance is", self.balance)

account = balance("1000$")  
account.check_balance()   
account.realbalance()   