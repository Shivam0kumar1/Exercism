import textwrap, re
Alphabets = "abcdefghijklmnopqrstuvwxyz"
def encode(plain_text):
    groups = textwrap.wrap(reverse(plain_text),5)
    result = " ".join(groups)
    return result


def decode(ciphered_text):
    return reverse(ciphered_text)

def reverse(text):
    text = text.replace(" ","").lower()
    result = ""
    for ch in text:
        if ch in Alphabets:
            result += Alphabets[-(Alphabets.index(ch)+1)]
        elif re.search(r"[0-9]+",ch):
            result+=ch
    return result
