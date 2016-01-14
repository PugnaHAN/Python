# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
This module provides the Transaction.

>>> a = Transaction(100, '2016-01-16', description = "current")
>>> a
Transaction(100, '2016-01-16', 'USD', 1, 'current', 100.0)
"""

TRANSACTION_STR = "Transaction({amount}, '{date}', '{currency}', {rate}, '{description}', {usd})"

import pickle

class Transaction:
    
    def __init__(self, amount, date, currency = 'USD',
                 usd_conversion_rate = 1, description = None):
        """
        this method is used to initial data
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description
        self.__usd = float(amount * usd_conversion_rate)

    @property
    def amount(self):
        """Return the amount of transaction
        >>> a = Transaction(100, '2016-01-16', description = "current")
        >>> a.amount
        100
        """
        return self.__amount

    @property
    def date(self):
        """Return the date of transaction
        >>> a = Transaction(100, '2016-01-16', description = "current")
        >>> a.date
        '2016-01-16'
        """
        return self.__date

    @property
    def currency(self):
        """Return the currency of transaction
        >>> a = Transaction(100, '2016-01-16', description = "current")
        >>> a.currency
        'USD'
        """
        return self.__currency

    @property
    def usd_conversion_rate(self):
        """Return the usd conversion rate of transaction
        >>> a = Transaction(100, '2016-01-16', description = "current")
        >>> a.usd_conversion_rate
        1.0
        """
        return float(self.__usd_conversion_rate)

    @property
    def description(self):
        """Return the description of transaction
        >>> a = Transaction(100, '2016-01-16', description = "current")
        >>> a.description
        'current'
        """
        return self.__description

    @property
    def usd(self):
        """Return the US Dollar of transaction
        >>> a = Transaction(100, '2016-01-16', description = "current")
        >>> a.usd
        100.0
        """
        return float(self.amount * self.__usd_conversion_rate)
   
    def __str__(self):
        """Return a humman readable string version of the transaction; the
        reuslt could be very long

        >>> a = Transaction(100, '2016-01-16', description = "current")
        >>> print(a)
        Transaction(100, '2016-01-16', 'USD', 1, 'current', 100.0)
        """
        return TRANSACTION_STR.format(amount = self.__amount,
                                      date = self.__date,
                                      currency = self.__currency,
                                      description = self.__description,
                                      rate = self.__usd_conversion_rate,
                                      usd = self.__usd)
    
    def __repr__(self):
        return  TRANSACTION_STR.format(amount = self.__amount,
                                       date = self.__date,
                                       currency = self.__currency,
                                       description = self.__description,
                                       rate = self.__usd_conversion_rate,
                                       usd = self.__usd)


class Account:
    """
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """


    
    def __init__(self, number, name):
        self.__number = number
        self.__name = name
        self.__transactions = []

    @property
    def number(self):
        """ The read only member
        """
        return self.__number

    @property
    def name(self):
        """The account's name

        This can be changed since it is only for human convenience;
        the account number is the true identifier.
        """
        return self.__name
    
    @name.setter
    def name(self, name):
        assert len(name) > 3
        self.__name = name

    def __len__(self):
        """Return the number of transactions
        """
        return len(self.__transactions)
    
    def apply(self, transaction):
        """Applies (adds) the given transaction to the account
        """
        self.__transactions.append(transaction)

    @property
    def balance(self):
        "Returns the balance in the USD"
        total = 0.0
        for transaction in self.__transactions:
            total += transaction.usd
        return total

    @property
    def all_usd(self):
        "Returns True if all the transactions are in the USD"
        for transaction in self.__transactions:
            if transaction.currency != 'USD':
                return False
        return True
    
    def save(self):
        "Saves the accout's data in the file name.acc"
        fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(self.name + ".acc", 'wb')
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()
    
    def load(self):
        """Loads the account's data from file name.acc

        All previous data is lost
        """
        fh = None
        try:
            fh = open(self.name + ".acc", 'rb')
            data = pickle.load(fh)
            assert self.number == data[0], "account number doesn't match"
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)    
