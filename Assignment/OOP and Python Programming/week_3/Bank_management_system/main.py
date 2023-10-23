from Bank import Bank
from Users import SavingsAccount, CurrentAccount, AdminAccount


def main():
    bank = Bank("Bangladesh Bank", 2000000)
    currentUser = None
    while (True):
        if (currentUser == None):
            print("\nNo user found !!!\n")
            print(f"A Bank has been created {bank.name}")
            ch = input("login or Register (L/R) : ")
            if (ch == "R"):
                acc_name = input("Account Name : ")
                acc_email = input("Account email : ")
                acc_address = input("Account Address : ")
                acc_password = input("Account Password : ")
                acc_type = input(
                    "press (sv/cu) sv for savings and cu for current : ")

                if (acc_type == "sv"):
                    acc_interest = int(input("Interest Rate : "))
                    currentUser = SavingsAccount(
                        bank, acc_name, acc_password, acc_email, acc_address, acc_interest)
                    bank.create_new_account(currentUser)
                else:
                    acc_limit = int(input("Overdraft Limit : "))
                    currentUser = CurrentAccount(
                        bank, acc_name, acc_password, acc_email, acc_address, acc_limit)
                    bank.create_new_account(currentUser)
            else:
                print("1. Admin Login : ")
                print("2. User Login : ")
                op = int(input("Choose Option : "))
                if (op == 1):
                    currentUser = AdminAccount(bank)
                    admin_pass = int(
                        # pass - 1234
                        input("To verify please put password : "))
                    if (currentUser.password != admin_pass):
                        print("\n--##--Invalid Admin Pass--##--\n")
                        return
                else:
                    acc_no = input("Account number : ")
                    for account in bank.accounts:
                        if (account.account_number == acc_no):
                            currentUser = account
                            break
        else:
            if (currentUser.type != "admin"):
                print(f"##-- Welcome back !! Your account number is: ",
                      {currentUser.account_number})
            if (currentUser.type == "savings"):
                print("1. Show info")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Apply Interest")
                print("5. Available Balance")
                print("6. Transaction History")
                print("7. Take loan")
                print("8. Money transfer")
                print("9. Logout")

                op = int(input("Choose Option : "))

                if (op == 1):
                    currentUser.account_info()
                elif (op == 2):
                    amount = int(input("Amount : "))
                    currentUser.deposit(amount)
                elif (op == 3):
                    amount = int(input("Amount : "))
                    currentUser.withdraw(amount)
                elif (op == 4):
                    currentUser.apply_interest()
                elif (op == 5):
                    currentUser.show_balance()
                elif (op == 6):
                    currentUser.check_transaction_history()
                elif (op == 7):
                    amount = int(input("Amount : "))
                    currentUser.take_loan(amount)
                elif (op == 8):
                    acc_no = input("Client Account Number : ")
                    amount = int(input("Amount : "))
                    currentUser.transfer_money(acc_no, amount)
                elif (op == 9):
                    currentUser = None
            elif (currentUser.type == "current"):
                print("1. Show info")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Available Balance")
                print("5. Transaction History")
                print("6. Take loan")
                print("7. Money transfer")
                print("8. Logout")

                op = int(input("Choose Option : "))

                if (op == 1):
                    currentUser.account_info()
                elif (op == 2):
                    amount = int(input("Amount : "))
                    currentUser.deposit(amount)
                elif (op == 3):
                    amount = int(input("Amount : "))
                    currentUser.withdraw(amount)
                elif (op == 4):
                    currentUser.show_balance()
                elif (op == 5):
                    currentUser.check_transaction_history()
                elif (op == 6):
                    amount = int(input("Amount : "))
                    currentUser.take_loan(amount)
                elif (op == 7):
                    acc_no = input("Client Account Number : ")
                    amount = int(input("Amount : "))
                    currentUser.transfer_money(acc_no, amount)
                elif (op == 8):
                    currentUser = None
            elif (currentUser.type == "admin"):
                print(f"\n!!---###-- Hi, Admin ---###--!!\n")
                print("1. Delete an user")
                print("2. See All accounts")
                print("3. Check total balance of the Bank")
                print("4. Check total loan amount")
                print("5. On or off loan feature (True/False)")
                print("6. Show Info")
                print("7. Check all the bank transaction")
                print("8. Set Bankrupt (True/False)")
                print("9. Logout")

                op = int(input("Choose Option : "))

                if (op == 1):
                    acc_num = input("Account no : ")
                    currentUser.delete_account(acc_num)
                elif (op == 2):
                    currentUser.see_all_accounts()
                elif (op == 3):
                    currentUser.show_balance()
                elif (op == 4):
                    currentUser.show_total_loan()
                elif (op == 5):
                    isGranted = bool(input("True or False : "))
                    currentUser.loan_granted_or_not(isGranted)
                elif (op == 6):
                    currentUser.account_info()
                elif (op == 7):
                    currentUser.check_all_bank_transaction()
                elif (op == 8):
                    isBankrupt = bool(input("True or False : "))
                    currentUser.set_bankrupt_or_not(isBankrupt)
                elif (op == 9):
                    currentUser = None


if (__name__ == "__main__"):
    main()
