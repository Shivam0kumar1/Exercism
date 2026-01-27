import re
def is_valid(isbn):
    isbn= isbn.replace("-","")
    if not re.search(r"^\d{9}[\dXx]$",isbn):
        return False
    total=0
    for index,number in enumerate(isbn):
        value =10 if number in "xX" else int(number)
        total += value*(len(isbn)-index)
    return total%11==0

        
