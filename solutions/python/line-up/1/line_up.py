tens=[11,12,13,14,15,16,17,18,19]
number_dictionary = {
    1:"st",
    2:"nd",
    3:"rd"
}
def line_up(name, number):
    if number in tens or str(number)[-1] == "0" or int(str(number)[-2:]) in tens:
        return (f"{name}, you are the {number}th customer we serve today. Thank you!")
    elif number%10 in number_dictionary:
        return (f"{name}, you are the {number}{number_dictionary[number%10]} customer we serve today. Thank you!")
    else:
        return (f"{name}, you are the {number}th customer we serve today. Thank you!")
        
