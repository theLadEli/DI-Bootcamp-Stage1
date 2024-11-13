class BankAccount:
    ACCOUNT_AVAILABLE_NUMBER = 1000 # Class attribute
    BANK_NAME = 'Hapoalim'

    def __init__(self, owner_name, balance=0):
        self.__owner_name = owner_name  # Private
        self.account_number = BankAccount.ACCOUNT_AVAILABLE_NUMBER
        self.transactions = []
        self.balance = balance
        BankAccount.ACCOUNT_AVAILABLE_NUMBER += 1

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount, currency = 'NIS'):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            if currency == "USD":
                amount = self.conversion(amount, 3.77)
                self.balance += amount
                self.transactions.append(f"Deposit: {amount}")
                print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)
    
    @staticmethod
    def conversion(amount, rate):
        return amount * rate

my_account = BankAccount("Eli")
print(my_account.account_number)

my_account.deposit(100,"USD")
my_account.balance()

second_account = BankAccount("Smith")
print(second_account.account_number)

third_account = BankAccount("Jack")
print(third_account.account_number)

fourth_account = BankAccount("Henry")
print(fourth_account.account_number)