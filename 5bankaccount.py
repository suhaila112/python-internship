class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.history=[]
    def deposite(self,amount):
        self.balance +=amount
        self.history.append(f"deposited :{amount}")
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientFundsError("Insufficient balance")
            self.balance-=amount
            self.history.append(f"withdraw: {amount}")
        else: 
            print("insufficient balance")
    def get_balance(self):
        return self.balance
    def transaction_history(self):
        for transaction in self.history:
            print(transaction)
    def __str__(self):
        return f"owner: {self.owner}, balance: {self.balance}"
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
        if self.balance-amount<-self.overdraft_limit:
            raise InsufficientFundsError("overdraft limit exceeded")
        self.balance -= amount
        self.history.append(f"withdraw: {amount}")
print("BANK ACCOUNT")
acc=BankAccount("tom",1000)
acc.deposite(500)
acc.withdraw(300)
print(acc)
print("balance: ",acc.get_balance())
print("\nTransaction History: ")
acc.transaction_history()
print("\nSAVINGS ACCOUNT")
savings=SavingsAccount("sara",2000,5)
print("before interest:" ,savings.get_balance())
savings.apply_interest()
print("after interest: ",savings.get_balance())
print("\nCURRENT ACCOUNT")
current =CurrentAccount("tom",1000,500)
current.withdraw(1200)
print(current)
print("balance: ",current.get_balance())
print("\nTransaction history: ")
current.transaction_history()
print("\nERROR TESTS")
try:
      acc.withdraw(5000)
except InsufficientFundsError as e:
      print("error: ",e)
try:
    current.withdraw(1000)
except InsufficientFundsError as e:
    print("error: ",e)
