class Bank:
    def __init__(self):
        # we wanna store the same information we stored before,
        # but as attributes of our class
        self.accounts = 
        self.balances = 

    def check_balance(self, account_name):
        # here, we can check the index of account_name in accounts,
        # and use that to find the balance of that account

    def add_account(self, account_name, initial_balance):
        # here, we add account_name to self.accounts and
        # add intial_balance to self.balances

    def make_transfer(self, from_account, to_account, amount):
        # use our check_balance() function to make sure that we have 
        # enough in from_account to make the transfer
        # then, subtract that from from_account and add it to to_account
