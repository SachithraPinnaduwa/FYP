import datetime
class BankAccount:
    def __init__(self, owner: str, balance: float=0.0):
        self.owner = owner
        self.balance = balance
        self.history = []
    def deposit(self, amt: float):
        if amt > 0:
            self.balance += amt
            self.history.append(("DEP", amt, datetime.datetime.now()))
