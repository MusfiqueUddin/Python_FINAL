class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.bank_balance: float = 0
        self.account_list = []
        self.admin_list = []
        self.loan_feature = True
        self.loan_amount = 0
