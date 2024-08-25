from user import User
from bank import Bank

class Admin:
    def __init__(self, name, pin, bank: Bank) -> None:
        self.bank = bank
        self.name = name
        self.pin = pin

    
    def create_account(self, name, email, address, account_type,bank: Bank):
        new_user = User(name, email, address, account_type)
        bank.account_list.append(new_user)
        print(f"YOUR ACCOUNT NUMBER IS : {new_user.account_number} (PLEASE REMEMBER)\n\n")

    
    
    def delete_account(self, account_number,bank: Bank):
        for acc in bank.account_list:
            if account_number == acc.account_number:
                bank.account_list.remove(acc)
                print(f"Account {account_number} deleted successfully!\n\n")
                return
        print(f"Account {account_number} not found.\n\n")

    
    
    def see_account_list(self,bank: Bank):
        print("ALL ACCOUNT LIST:")
        for account in bank.account_list:
            print(f"Name: {account.name}    Account Number: {account.account_number}    Account Type: {account.account_type}")

    
    
    def bank_balance(self,bank: Bank):
        print(f"TOTAL BANK BALANCE = {bank.bank_balance} TAKA\n\n")

    
    
    def loan_amount(self,bank: Bank):
        print(f"TOTAL LOAN AMOUNT = {bank.loan_amount} TAKA\n\n")

    
    
    def loan_feature(self, on_off: bool,bank: Bank):
        bank.loan_feature = on_off
        status = "enabled" if on_off else "disabled"
        print(f"Loan feature has been {status}.\n\n")
