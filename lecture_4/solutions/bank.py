class Bank:
    def __init__(self):
        # we wanna store the same information we stored before,
        # but as attributes of our class
        self.accounts = []
        self.balances = []

    def check_balance(self, account_name):
        # here, we can check the index of account_name in accounts,
        # and use that to find the balance of that account
        i = 0
        while self.accounts[i] != account_name:
            i = i + 1

        return(self.balances[i])

    def add_account(self, account_name, initial_balance):
        # here, we add account_name to self.accounts and
        # add intial_balance to self.balances
        self.accounts.append(account_name)
        self.balances.append(initial_balance)

    def make_transfer(self, from_account, to_account, amount):
        # use our check_balance() function to make sure that we have 
        # enough in from_account to make the transfer
        # then, subtract that from from_account and add it to to_account
        if self.check_balance(from_account) > amount:
            # we have enough in the from account to make the transfer

            # let's caclulate our indexes
            # this is the same code as the while loop in check_balances()
            # but with a built in function called index()
            index_from_account = self.accounts.index(from_account)
            index_to_account = self.accounts.index(to_account)

            self.balances[index_from_account] = self.balances[index_from_account] - amount
            self.balances[index_to_account]   = self.balances[index_to_account]   + amount
