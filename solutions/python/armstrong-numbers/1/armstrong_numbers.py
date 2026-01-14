def is_armstrong_number(number):
    str_number = str(number)
    length = len(str_number)
    sum = 0
    for i in str_number:
        sum+=(pow(int(i),length))
    return sum == number
