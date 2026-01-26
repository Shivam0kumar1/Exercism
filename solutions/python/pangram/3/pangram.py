import re
def is_pangram(sentence):
    # if not sentence: return False
    # return sum(1 for i in set(sentence.upper()) if re.match(r"^[a-zA-Z]*$",i)) == 26
    return bool(sentence and sum(1 for i in set(sentence.upper()) if re.match(r"^[a-zA-Z]*$",i)) == 26)

