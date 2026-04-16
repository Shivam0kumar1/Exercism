def rows(letter):
    length = ord(letter)-ord("A")+1 #This if for counting spaces
    result = []
    for i in range(length):
        outer = " "*(length-i-1)
        char = chr(ord("A")+i)
        if i==0:
            row = outer+char+outer
        else:
            inner = " "*(2*i-1)
            row = outer+char+inner+char+outer
        result.append(row)
    result+=result[-2::-1]
    return result
        
        
