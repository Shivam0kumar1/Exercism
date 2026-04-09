vowels = ['a','e','i','o','u','xr','yt']
def translate(text):
    words = text.split()    #Split sentence into words
    result = [translate_word(word) for word in words]
    return " ".join(result)

def translate_word(text):
    find_qu = text.find("qu")
    find_y = text.find("y")
    result=text
    # find_consonant = text.find(str(vowels))
    if text[0] in vowels or text[0]+text[1] in vowels:
        return (text+ "ay")
    elif text[0] not in vowels:
        for char in text:
            if char in vowels and (text.find(char)<=find_qu or find_qu<0) and (text.find(char)<=find_y or find_y<=0):
                find_consonant = text.find(char)
                result = text[find_consonant:]+text[:find_consonant]+"ay"
                # return text
                break
    if find_qu>=0 and result==text:
        result=text[find_qu+2:]+text[:find_qu+2]+"ay"
    elif find_y>0 and result == text:
        result=text[find_y:]+text[:find_y]+"ay"
    # else:
    #     result = text[1:]+text[0]+"ay"
    return result
