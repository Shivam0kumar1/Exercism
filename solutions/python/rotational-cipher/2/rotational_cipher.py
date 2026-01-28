def rotate(text, key):
    """Simplified Version"""
    # new_text = ""
    # for character in text:
    #     if character.isalpha():
    #         sum_ascii_value = ord(character)+key
    #         if sum_ascii_value>122 and character.islower():
    #             sum_ascii_value = sum_ascii_value-122+96
    #         if sum_ascii_value>90 and character.isupper():
    #             sum_ascii_value = sum_ascii_value-90+64
    #         new_text+=chr(sum_ascii_value)
    #     else:new_text+=character
    # return new_text
    
    """More optimised Version"""
    new_text = ""
    for character in text:
        if character.isalpha():
            base = ord("a") if character.islower() else ord("A")
            new_text+=chr((ord(character)-base+key)%26+base)
        else: new_text+=character
    return new_text
    
