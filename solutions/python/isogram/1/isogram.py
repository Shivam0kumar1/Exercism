def is_isogram(string):
    string = string.lower()
    string = string.replace(" ","")
    string = string.replace("-","")
    new_string = set(string)
    return len(new_string)==len(string)
