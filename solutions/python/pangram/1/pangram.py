import re
def is_pangram(sentence):
    sentence = set(sentence.upper())
    pattern = r"^[a-zA-Z]*$"
    count=0
    for i in sentence:
        if re.match(pattern,i):
            count+=1
    if count == 26:
        return True
    return False
