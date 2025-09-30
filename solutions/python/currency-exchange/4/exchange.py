"""Functions for calculating steps in exchanging currency."""



def exchange_money(budget: float, exchange_rate: float) ->float:
    """Calculate foreign currency value after exchange.
    Args:
        budget: amount of money planning to exchange.
        exchange_rate: amount of domestic currency equal to 1 unit of foreign currency
    Returns:  Value of exchange currency
    """
    return budget/exchange_rate


def get_change(budget: float, exchanging_value: float)-> float:
    """Calculate amount of money left from budget
    Args:
        budget: Amoount of money before exchange
        exchanging_value: Amount taken from budget to be exchanged
    Returns: Remaining money
    """
    return budget-exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int)->int:
    """Calculate total value of bills from the booth (excluding fractional amount).
    Args:
        denomination: Value of a single bill.
        number_of_bills: Total number of bills.
    Returns: Total bill value kept by the customer.
    """
    return denomination*number_of_bills


def get_number_of_bills(amount: float, denomination: int)->int:
    """Calculate number of currency bills that can be received from given amount(only whole bills         not fractions of bills).
    Args:
        amount: total amount available from which bills will be generated.
        denomination: whole  bill of currency, that needs to be taken from amount
    Returns: Number of currency bills
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: int)->float:
    """Calculate leftover amount that can't be returned from starting amount given the                    denomination of bills.
    Args:
        amount: total amount available from which bills will be generated.
        denomination: whole  bill of currency, that is taken from amount.
    Returns: Remaining amount after full bills are used.  
    """
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int)->int:
    """Calculate maximum value of the new currency after applying exchange rate and spread.
    Args:
        Spread: Percentage takes as an exchange fee.
    Returns: Maximum value of new currency.
    """

    #Apply spread to calculate actual rate
    actual_rate = exchange_rate*(1+spread/100)

    # Calculate total foreign currency
    foreign_currency = budget/actual_rate

    # Return value after rounding down to nearest denomination
    return int(foreign_currency//denomination)*denomination
