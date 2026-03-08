def flatten(iterable):
    result=[]
    for i in iterable:
        if (isinstance(i,(list,str,tuple,dict,set)) and len(i)==0) or i==None:
            continue
        elif isinstance(i,(list,tuple,str,dict,set)):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
