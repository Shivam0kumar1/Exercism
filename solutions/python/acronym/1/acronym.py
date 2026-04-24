def abbreviate(words):
    words = words.replace("-"," ")
    words = words.replace("_"," ")
    result = "".join(word[0] for word in words.split())
    return result.upper()
