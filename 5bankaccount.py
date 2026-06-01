class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.history=[]
    def deposite(self,amount):
        self.balance +=amount
        self.history.append(f"deposited :{amount}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.history.append(f"withdraw: {amount}")
        else: 
            print("insufficient balance")
    def get_balance(self):
        return self.balance
    def transaction_history(self):
        for transaction in self.history:
            print(transaction)
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super(). __init__(owner,balance)
        self.interest_rate=interest_rate
    def apply_interest(self):
        interest=self.balance* self.interest_rate /100
        self.balance +=interest
        self.history.append(f"interest added: {interest}")
class CurrentAccount(BankAccount):
    def __init__(self,owner,balance,overdraft_limit):
        super(). __init__(owner,balance)
        self.overdraft_limit=overdraft_limit
    def withdraw(self,amount):
        if amount<=self.balance + self.overdraft_limit:
            self.balance -= amount
            self.history.append(f"withdraw: {amount}")
        else:
            print("overdraft limit exceeded")
s1=SavingsAccount("john",10000,5)
s1.deposite(1000)
s1.withdraw(2000)
s1.apply_interest()
print("balance:",s1.get_balance())
s1.transaction_history()
c1=CurrentAccount("ali",5000,1000)
c1.withdraw(5500)
print("balance:",c1.get_balance())
c1.transaction_history()        