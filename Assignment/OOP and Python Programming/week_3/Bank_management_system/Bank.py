class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.isBankrupt = False
        self.accounts = []
        self.isLoanGranted = True
        self.total_loan_taken = 0
        self.balance = balance

    def create_new_account(self, account):
        unique_account_number = f"{account.name}-{len(self.accounts) + 1}"
        account.account_number = unique_account_number
        self.accounts.append(account)
