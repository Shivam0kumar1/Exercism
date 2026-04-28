def slices(series, length):
    if length==0:
        raise ValueError("slice length cannot be zero")
    elif length<0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    elif length>len(series):
        raise ValueError("slice length cannot be greater than series length")
    result = []
    for i in range(len(series)+1-length):
        result.append(series[i:i+length])
    return result
        