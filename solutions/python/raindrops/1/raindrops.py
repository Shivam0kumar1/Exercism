def convert(number):
    output = ""
    flag=True
    remainder_three,remainder_five,remainder_seven = number%3,number%5,number%7
    if remainder_three==0:
        output+="Pling"
        flag=False
    if remainder_five == 0:
        output+="Plang"
        flag=False
    if remainder_seven == 0:
        output+="Plong"
        flag=False
    if flag:
        output = str(number)
    return output
