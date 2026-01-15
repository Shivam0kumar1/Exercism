"""Version 1"""
# import re
# def response(hey_bob):
#     hey_bob = hey_bob.strip()
#     if hey_bob=="":
#         return "Fine. Be that way!"
#     else:
#         if "?" not in hey_bob[-1] and hey_bob == hey_bob.upper() and re.search(r'[a-zA-Z]',hey_bob):
#             return "Whoa, chill out!"
#         elif "?" in hey_bob[-1] and hey_bob == hey_bob.upper() and re.search(r'[a-zA-Z]',hey_bob):
#             return "Calm down, I know what I'm doing!"
#         elif "?" in hey_bob[-1]:
#             return "Sure."
#         return "Whatever."

"""Version 2"""
def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob=="":
        return "Fine. Be that way!"
    else:
        if "?" not in hey_bob[-1] and hey_bob.isupper():
            return "Whoa, chill out!"
        elif "?" in hey_bob[-1] and hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        elif "?" in hey_bob[-1]:
            return "Sure."
        return "Whatever."
