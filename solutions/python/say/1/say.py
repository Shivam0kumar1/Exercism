NUMBERS = {
    0: "zero",    1: "one",    2: "two",    3: "three",    4: "four",    5: "five",
    6: "six",    7: "seven",    8: "eight",    9: "nine",    10: "ten",
    11: "eleven",    12: "twelve",    13: "thirteen",    14: "fourteen",
    15: "fifteen",    16: "sixteen",    17: "seventeen",    18: "eighteen",
    19: "nineteen"
}
TENS = {
    2: "twenty",    3: "thirty",    4: "forty",    5: "fifty",
    6: "sixty",    7: "seventy",    8: "eighty",    9: "ninety"
}
PLACE_VALUES = ["thousand","million","billion"]

# Method1
def single_digits(number):
    return NUMBERS[number]

def tens_place(number):
    if number<20:
        return NUMBERS[number]
    else:
        result=""
        if number%10!=0:
            result= "-"+NUMBERS[number%10]
        result = TENS[number//10]+result
    return result
def under_thousand(number):
    result = ""
    if len(str(number))==1:
        result = single_digits(number)
    elif len(str(number))==2:
        result = tens_place(number)
    else:
        if number%100!=0:
            result=" "+tens_place(number%100)
        result = NUMBERS[number//100]+" hundred"+result
    return result
    
def say(number):
    if number<0 or number>999999999999:
        raise ValueError("input out of range")
    elif number==0:
        return "zero"
    str_num = str(number)
    new_list = []
    for i in range(len(str_num),0,-3):
        new_list.append(int(str_num[max(0, i-3):i]))
        print("a:",new_list)
    print(new_list)
    # new_list.reverse()
    print(new_list)
    result = ""
    i=0
    for num in new_list:
        if i==0 and num!=0:
            result = under_thousand(num)
            print(num," ",result," und0 ",under_thousand(num))
        elif num!=0:
            result = under_thousand(num)+ " "+ PLACE_VALUES[i-1] + " " +result
            print(num," ",result," und ",under_thousand(num))
        i+=1
    return result.strip()