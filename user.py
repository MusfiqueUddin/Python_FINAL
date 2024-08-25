from bank import Bank
import random
class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = str(random.randint(10000, 99999))
        self.transaction_history_list = []
        self.loan_count = int(0)
        

    
    
    def deposit(self, amount,bank: Bank):
        amount = float(amount)
        if amount <= 0:
            print("Please Choose Higher Amount.\n\n")
            return

        self.balance += amount
        bank.bank_balance += amount
        self.transaction_history_list.append(f"Deposited: {amount}")
        print(f"Deposited {amount} TAKA successfully.\n\n")

    
    
    def withdraw(self, amount,bank: Bank):
        amount = float(amount)
        if amount <= 0:
            print("Please Choose Higher Amount.\n\n")
            return
        
        if amount > self.balance:
            print("Insufficient balance.\n\n")
            return
        
        if amount > bank.bank_balance:
            print("The bank is bankrupt.\n\n")
            return
        
        self.balance -= amount
        bank.bank_balance -= amount
        self.transaction_history_list.append(f"Withdrew: {amount}")
        print(f"Withdrawn {amount} TAKA successfully.\n\n")
    
    
    
    def check_balance(self):
        print(f'Available balance = {self.balance} TAKA\n\n')

    
    def transaction_history(self):
        if not self.transaction_history_list:
            print("No transaction history available.\n\n")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history_list:
                print(transaction)

    
    
    
    
    def take_loan(self, amount,bank: Bank):
        amount = float(amount)
        if self.loan_count >= 2:
            print(" No more loans can be taken.\n\n")
            return

        if bank.loan_feature:
            if  bank.bank_balance >= amount:
                self.balance += amount
                bank.bank_balance -= amount
                self.loan_count += 1
                bank.loan_amount += amount
                print(f"Loan of {amount} TAKA taken successfully.\n\n")
            else:
                print(f"You cannot take a loan more than {bank.bank_balance} TAKA.\n\n")
        else:
            print("Loan feature is currently not available.\n\n")

    
    
    
    def transfer_money(self, receiver_account, amount):
        amount = float(amount)
        if amount <= 0:
            print("Please Enter Higher Amount\n\n")
            return

        if amount > self.balance:
            print("Insufficient balance.\n\n")
            return

        self.balance -= amount
        receiver_account.balance += amount
        self.transaction_history_list.append(f"Transferred: {amount} TAKA to account {receiver_account.account_number}")
        print(f"Transfer of {amount} TAKA to account {receiver_account.account_number} successful.\n\n")

