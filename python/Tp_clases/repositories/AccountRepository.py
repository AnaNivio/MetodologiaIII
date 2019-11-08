from models.Client import Client
from models.Account import Account


class AccountRepository:
    def __init__(self):
        self._id = 1
        self._account_array = {}

    def save(self, account: Account):
        self._account_array[self._id] = account
        self._id = self._id + 1

    def get(self):
        for i in range(len(self._account_array)):
            account = self._account_array[i+1]
            print(account.to_string())
