def square(number):
    if 1>number or number>64:
        raise ValueError("square must be between 1 and 64")
    else:
        return pow(2,number-1)

def total():
    return sum(square(n) for n in range(1,65))
