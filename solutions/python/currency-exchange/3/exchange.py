"""Functions for calculating steps in exchanging currency."""



def exchange_money(budget: float, exchange_rate: float) ->float:
    """This function returns the value of exchanged currency
    budget: amount of maney planning to exchange.
    exchange_rate: amount of domestic currency equal to 1 unit of foreing currency
    """
    return budget/exchange_rate


def get_change(budget: float, exchanging_value: float)-> float:
    """Return amount of money left from budget
    budget: Amoount of money before exchange
    exchanging_value: Amount taken from budget to be exchanged
    """
    return budget-exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int)->int:
    """Returns the total value  of bill from the booth(excluding fractional amount, which is kept by         the booth)
    denomination: Value of a signle bill.
    number_of_bills: Total number of bills"""
    return denomination*number_of_bills


def get_number_of_bills(amount: float, denomination: int)->int:
    """Returns the number of currency bills that can be received from given amount(only whole bills       not fractions of bills).
    amount: total amount available from which bills will be generated.
    denomination: whole  bill of currency, that needs to be taken from amount"""
    return amount // denomination


def get_leftover_of_bills(amount: float, denomination: int)->float:
    """Returns the leftover amount that cann't be returned from starting amount given the                    denomination of bills.
    amount: total amount available from which bills will be generated.
    denomination: whole  bill of currency, that is taken from amount"""
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int)->int:
    """This function return the maximum value of the new currency after calculating the                      exchange rate plus the spread.
    Spread: Percentage takes as an exchange fee"""

    #Adding spread to calculate actual rate
    actual_rate = exchange_rate*(1+spread/100)

    # Calculate total foreign currency
    foreign_currency = budget/actual_rate

    # Return value after rounding down to nearest denomination
    return int(foreign_currency//denomination)*denomination
