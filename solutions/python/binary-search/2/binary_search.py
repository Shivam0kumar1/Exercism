def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")
    index=len(search_list)//2
    mid_value = search_list[index]
    if mid_value<value:
        return index+1+find(search_list[index+1:],value)
    if mid_value>value:
        return find(search_list[:index],value)
    return index
