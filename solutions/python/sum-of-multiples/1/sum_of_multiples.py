def sum_of_multiples(limit, multiples):
    result= set()
    for element in multiples:
        if element==0:
            continue
        for multiple in range(element,limit,element):
            result.add(multiple)
    return sum(result)
