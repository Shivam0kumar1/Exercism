import re
def abbreviate(words):
    # words = words.replace("-"," ")
    # words = words.replace("_"," ")
    # result = "".join(word[0] for word in words.split())
    # return result.upper()

    return "".join(word[0].upper() for word in re.findall(r"[a-zA-Z']+",words))
