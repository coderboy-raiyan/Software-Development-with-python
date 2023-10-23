from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, bank, name, password, email, address, type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.type = type
        self.bank = bank
        self.transaction_history = []
        self.account_number = None
        self.balance = 0
        self.loan_limit = 2

    def show_balance(self):
        print(self.balance)

    def deposit(self, amount):
        if (amount >= 0):
            self.balance += amount
            history = f"Deposit done by {self.account_number}", amount
            self.transaction_history.append(history)
            print("\n---###--- Deposit Done. New Balance is ---###---\n", self.balance)
        else:
            print("\n---###--- Invalid amount ---###---\n")

    def withdraw(self, amount):
        if (self.bank.isBankrupt):
            print("\n---###-- Bank is bankrupt ---###--\n")
            return
        if (amount >= 0 and amount <= self.balance):
            self.balance -= amount
            history = f"Withdrawal done by {self.account_number}", amount
            self.transaction_history.append(history)
            print("\n---###--- Withdraw Done. New Balance is ---###---\n", self.balance)
        else:
            print("\n---###--- Withdrawal amount exceeded ---###---\n")

    def transfer_money(self, account_no, money):
        isExists = False
        for account in self.bank.accounts:
            if (account.account_number == account_no):
                if (money >= 0 and money <= self.balance):
                    history = f"Transaction done by {
                        self.account_number}", money
                    self.transaction_history.append(history)
                    account.deposit(money)
                    self.balance -= money
                    print(
                        "\n---###--- Mony Transfer Done. New Balance is ---###---\n", self.balance)
                    isExists = True
                    break
                else:
                    print("\n---###--- Insufficient Balance ---###---\n")
        if (isExists is not True):
            print("\n---###--- Account does not exist ---###---\n")

    def take_loan(self, amount):
        if (self.loan_limit >= 1 and amount <= self.bank.balance):
            if (self.bank.isLoanGranted):
                self.balance += amount
                self.bank.balance -= amount
                self.bank.total_loan_taken += amount
                self.loan_limit -= 1
                history = f"Loan taken by {self.account_number}", amount
                self.transaction_history.append(history)
                print(
                    "\n---###--- Loan granted. New Balance is ---###---\n", self.balance)
            else:
                print(
                    "\n---###--- Loan is not Available. New Balance is ---###---\n")
        else:
            print("\n---###--- You have crossed your loan limit !!! ---###---\n")

    def check_transaction_history(self):
        print(
            f"##-- Here are all the transaction by {self.account_number} --##")
        for transaction in self.transaction_history:
            print(transaction)

    @abstractmethod
    def account_info(self):
        raise NotImplementedError


class SavingsAccount(Account):
    def __init__(self, bank, name, password, email, address, interestRate) -> None:
        super().__init__(bank, name, password, email, address, "savings")
        self.interestRate = interestRate

    def apply_interest(self):
        interest = self.balance * (self.interestRate / 100)
        self.balance += interest
        history = f"Interest Applied by {self.account_number}", interest
        self.transaction_history.append(history)
        print("\n---###--- Interest Done. New Balance is ---###---\n", self.balance)

    def account_info(self):
        print("\n--------####--------\n")
        print("Account Name : ", self.name)
        print("Account balance : ", self.balance)
        print("Account email : ", self.email)
        print("Account type : ", self.type)
        print("\n--------####--------\n")


class CurrentAccount(Account):
    def __init__(self, bank, name, password, email, address, limit) -> None:
        super().__init__(bank, name, password, email, address, "current")
        self.limit = limit

    def withdraw(self, amount):
        if (self.bank.isBankrupt):
            print("\n---###-- Bank is bankrupt ---###--\n")
            return
        if (amount >= 0 and amount <= self.limit):
            self.balance -= amount
            history = f"Withdrawal done by {self.account_number}", amount
            self.transaction_history.append(history)
            print("\n---###--- Withdraw Done. New Balance is ---###---\n", self.balance)
        else:
            print("\n---###--- Withdrawal amount exceeded ---###---\n")

    def account_info(self):
        print("\n--------####--------\n")
        print("Account Name : ", self.name)
        print("Account balance : ", self.balance)
        print("Account email : ", self.email)
        print("Account type : ", self.type)
        print("\n--------####--------\n")


class AdminAccount(Account):
    def __init__(self, bank) -> None:
        super().__init__(bank, "admin", 1234, "admin@admin.com", "", "admin")

    def delete_account(self, accNo):
        for account in self.bank.accounts:
            if (account.account_number == accNo):
                self.bank.accounts.remove(account)
                print(
                    f"\n---###-- This account {accNo} has been Deleted !!! ---###--\n")
                return
        print("\n---###-- Account not found !!!  ---###--\n")

    def see_all_accounts(self):
        for account in self.bank.accounts:
            print(f"""Account Name: {account.name} and Account Number: {
                  account.account_number}""")

    def show_balance(self):
        print("\n---###--- Bank Balance : ---###---\n ", self.bank.balance)

    def show_total_loan(self):
        print("\n---###---  Total loan amount : ---###---\n ",
              self.bank.total_loan_taken)

    def loan_granted_or_not(self, isGranted):
        self.bank.isLoanGranted = isGranted
        print("\n---###---  Loan setting has been changed to : ---###---\n ",
              self.bank.isLoanGranted)

    def check_all_bank_transaction(self):
        for account in self.bank.accounts:
            print(f"\n---###-- {account.name} account's history ---###-- \n")
            for history in account.transaction_history:
                print(history)

    def set_bankrupt_or_not(self, isBankrupt):
        self.bank.isBankrupt = isBankrupt
        print("\n---###---  Bankrupt setting has been changed to : ---###---\n ",
              self.bank.isBankrupt)

    def account_info(self):
        print("\n--------####--------\n")
        print("Account Name : ", self.name)
        print("Account balance : ", self.balance)
        print("Account email : ", self.email)
        print("Account type : ", self.type)
        print("\n--------####--------\n")
