def classify(number) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        # total=0
        # for n in range(1,number//2+1):
        #     if number%n==0:
        #         total+=n
        total = sum(i for i in range(1,number//2+1) if number%i==0)
        if total==number:
            return "perfect"
        elif total>number:
            return "abundant"
        else:
            return "deficient"

