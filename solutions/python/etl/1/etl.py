def transform(legacy_data):
    result={}
    for index, value in legacy_data.items():
        for letter in value:
            result[letter.lower()]=index
    return result
