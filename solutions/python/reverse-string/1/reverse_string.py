def reverse(text):
    reverse_string = ""
    for char in range(1,len(text)+1):
        reverse_string+=text[-char]
    return reverse_string
    # return "".join(text[-char] for char in range(1,len(text)+1))
