def is_armstrong_number(number: int) -> bool:
    str_number = str(number)
    length = len(str_number)
    """Method 1"""
    # sum = 0
    # for i in str_number:
    #     sum+=(pow(int(i),length))
    # return sum == number

    """Method 2"""
    # return sum(int(digit)**length for digit in str_number) == number

    """Method 3"""
    sum=0
    n=number
    while n>0:
        digit = n%10
        sum+=(digit**length)
        n//=10
    return sum==number
