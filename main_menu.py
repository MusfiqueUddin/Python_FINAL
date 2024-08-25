from bank import Bank
from admin import Admin
from user import User

# shuru
def main_menu():
    print(f"Welcome to {MusfiqueBank.name}\n")
    print("Please Log in as:\n1. User\n2. Admin\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        user_menu()
    elif choice == '2':
        admin_menu()

    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice.\n\n")
        main_menu()


# user er ta
def user_menu():
    if not MusfiqueBank.account_list:
        print("Create An User Account First. Select Admin Menu\n\n")
        main_menu()
    else:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Log Out")
    
        choice = input("Enter your choice: ")

        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            transfer_money()
        elif choice == '5':
            transaction_history()
        elif choice == '6':
            take_loan()
        elif choice == '7':
            main_menu()
        else:
            print("Invalid choice.\n\n")
            user_menu()




# admin er ta
admin_authenticated = False

def admin_menu():
    global admin_authenticated
    if not MusfiqueBank.admin_list:
        print("Be An Admin First.\n\n")
        ds = input("Create Admin Account: 1.YES  2.NO\n")
        if ds == '1':
            Aname = input("Enter Name: ")
            APin = input("Enter password: ")
            global my_admin
            my_admin = Admin(Aname, APin, MusfiqueBank)
            MusfiqueBank.admin_list.append(my_admin)
            print("Admin created successfully!\n\n")
            admin_authenticated = True
            admin_menu()
        else:
            print("Exiting to main menu...\n\n")
            main_menu()
    else:
        if not admin_authenticated:
            code = input("ENTER ADMIN PIN TO GET ACCESS: ")
            for admin in MusfiqueBank.admin_list:
                if code == admin.pin:
                    print("Admin Menu:")
                    admin_authenticated = True
                    break
            else:
                print("WRONG PIN")
                admin_menu()

        print("Admin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See Account List")
        print("4. Bank Balance")
        print("5. Loan Amount")
        print("6. Loan Feature Control")
        print("7. Log Out")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin_create_account()
        elif choice == '2':
            admin_delete_account()
        elif choice == '3':
            admin_see_account_list()
        elif choice == '4':
            admin_bank_balance()
        elif choice == '5':
            admin_loan_amount()
        elif choice == '6':
            admin_loan_feature()
        elif choice == '7':
            admin_authenticated = False
            main_menu()
        else:
            print("Invalid choice.\n\n")
            admin_menu()




def deposit():
    account_number = input("Enter your account number: ")
    amount = float(input("Enter deposit amount: "))
    for acc in MusfiqueBank.account_list:
        if account_number == str(acc.account_number):
            acc.deposit(amount,MusfiqueBank)
            break
    else:
        print("Account not found.\n\n")
    user_menu()





def withdraw():
    account_number = input("Enter your account number: ")
    amount = float(input("Enter withdrawal amount: "))
    for acc in MusfiqueBank.account_list:
        if account_number == acc.account_number:
            acc.withdraw(amount,MusfiqueBank)
            break
    else:
        print("Account not found.\n\n")
    user_menu()



def check_balance():
    account_number = input("Enter your account number: ")
    for acc in MusfiqueBank.account_list:
        if account_number == acc.account_number:
            acc.check_balance()
            break
    else:
        print("Account not found.\n\n")
    user_menu()




def transfer_money():
    sender_account_number = input("Enter your account number: ")
    receiver_account_number = input("Enter receiver's account number: ")
    amount = float(input("Enter amount to transfer: "))
    sender_acc = None
    receiver_acc = None
    for acc in MusfiqueBank.account_list:
        if sender_account_number == acc.account_number:
            sender_acc = acc
        if receiver_account_number == acc.account_number:
            receiver_acc = acc
    
    if sender_acc and receiver_acc:
        sender_acc.transfer_money(receiver_acc, amount)
    else:
        if not sender_acc:
            print("Sender account not found.\n\n")
        if not receiver_acc:
            print("Receiver account not found.\n\n")
    user_menu()




def transaction_history():
    account_number = input("Enter your account number: ")
    for acc in MusfiqueBank.account_list:
        if account_number == acc.account_number:
            acc.transaction_history()
            break
    else:
        print("Account not found.\n\n")
    user_menu()


def take_loan():
    account_number = input("Enter your account number: ")
    amount = input("Enter loan amount: ")
    for acc in MusfiqueBank.account_list:
        if account_number == acc.account_number:
            acc.take_loan(amount,MusfiqueBank)
            break
    else:
        print("Account not found.\n\n")
    user_menu()



def admin_create_account():
    name = input("Enter account holder's name: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    account_type = input("Enter account type (e.g., savings, checking): ")
    my_admin.create_account(name, email, address, account_type,MusfiqueBank)
    admin_menu()

def admin_delete_account():
    account_number = input("Enter account number to delete: ")
    my_admin.delete_account(account_number,MusfiqueBank)
    admin_menu()

def admin_see_account_list():
    my_admin.see_account_list(MusfiqueBank)
    admin_menu()

def admin_bank_balance():
    my_admin.bank_balance(MusfiqueBank)
    admin_menu()

def admin_loan_amount():
    my_admin.loan_amount(MusfiqueBank)
    admin_menu()

def admin_loan_feature():
    sts = input("Enable loan feature? (1.Yes  2.No): ")
    if sts == '1':
        my_admin.loan_feature(True,MusfiqueBank)
        admin_menu()
    elif sts == '2':
        my_admin.loan_feature(False,MusfiqueBank)
        admin_menu()


    
    
MusfiqueBank = Bank("Musfique Bank")
main_menu()
