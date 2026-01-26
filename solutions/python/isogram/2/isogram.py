def is_isogram(string):
    string = string.lower().replace(" ","").replace("-","")
    new_string = set(string)
    return len(new_string)==len(string)
