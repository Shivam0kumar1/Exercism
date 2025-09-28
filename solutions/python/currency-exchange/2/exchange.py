"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate) ->float:
    return budget/exchange_rate


def get_change(budget, exchanging_value)-> float:
    return budget-exchanging_value


def get_value_of_bills(denomination, number_of_bills)->int:
    return denomination*number_of_bills


def get_number_of_bills(amount, denomination)->int:
    return amount // denomination


def get_leftover_of_bills(amount, denomination)->float:
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination)->int:
    return int((budget/(exchange_rate*(1+spread/100))//denomination)*denomination)
