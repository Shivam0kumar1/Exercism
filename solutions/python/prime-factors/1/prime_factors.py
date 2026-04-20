def factors(value):
    result=[]
    i=2
    if value is 1:
        return []
    while value>1:
        if value%i==0:
            result.append(i)
            value//=i
        else:
            i+=1     
    return result
