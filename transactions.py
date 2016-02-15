import csv
import pandas as pd

class Transactions():
    def __init__(self, _transactions):
        self._transactions = _transactions

    def __getattr__(self, name):
        return eval('self._transactions.{}'.format(name))

    @classmethod
    def _from_csv(cls, csv_fn):
        return cls(pd.read_csv(csv_fn, parse_dates=['Date'],
            index_col=['Date']))

