class BalanceException(Exception):
    pass

class account:
    def __init__(self, initialAmnt : float, accountName: str):
        self.name = accountName
        self.balance = initialAmnt
        print(f"\nAccount created!\nName : {self.name}\nBalance : {self.balance:.2f} SEK!")

    def getBalance(self, end: str):
        print(f"\nCurrent balance of the account '{self.name}' :\n{self.balance:.2f} SEK", end=end)

    def deposit(self, amount: float):
        print(f"\n\n{amount:.2f} SEK has been deposited to the account '{self.name}'")
        self.getBalance()

    def validWithdraw(self, amount: float):
        if (self.balance > amount):
            pass
        else:
            raise BalanceException(f"\nSorry, your account does not have enough to withdraw {amount} SEK!")

    def withdraw(self, amount: float):
        try:
            self.validWithdraw(amount)
            print(f"{amount:.2f} has been withdrawn from the account '{self.name}'")
            self.balance -= amount
            self.getBalance()

        except BalanceException as error:
            print(f"Transaction iterrupted : {error}")