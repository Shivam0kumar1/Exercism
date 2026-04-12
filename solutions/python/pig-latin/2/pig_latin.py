vowels = ('a','e','i','o','u','xr','yt')
def translate(text):
    words = text.split()    #Split sentence into words
    result = [translate_word(word) for word in words]
    return " ".join(result)

def translate_word(text):
    # Rule1
    if text.startswith(vowels):
        return text+"ay"

    for i in range(len(text)):
        #Rule 3
        if text[i:i+2] == "qu":
            return text[i+2:]+text[:i+2]+"ay"

        #Rule 4
        if text[i] == "y" and i!=0:
            return text[i:]+text[:i]+"ay"

        if text[i].startswith(vowels):
            return text[i:]+text[:i]+"ay"
    
