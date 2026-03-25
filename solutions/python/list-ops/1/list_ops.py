def append(list1, list2):
    return list1+list2


def concat(lists):
    resulting_list=[]
    for sublist in lists:
        for item in sublist:
            resulting_list+=[item]
    return resulting_list


def filter(function, list):
    result=[]
    for item in list:
        if function(item):
            result+=[item]
    return result


def length(list):
    count=0
    for x in list:
        count+=1
    return count


def map(function, list):
    result=[]
    for item in list:
        # if function(item):
        result+=[function(item)]
    return result


def foldl(function, list, initial):
    acc=initial
    for item in list:
        acc = function(acc,item)
    return acc


def foldr(function, list, initial):
    acc=initial
    for item in reverse(list):
        acc = function(acc,item)
    return acc


def reverse(list):
    result=[]
    for item in list:
        result=[item]+result
    return result
