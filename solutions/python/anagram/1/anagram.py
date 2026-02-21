def find_anagrams(word, candidates):
    result = []
    word = word.lower()
    
    for word2 in candidates:
        dict1={}
        dict2={}
        word3 = word2.lower()
        is_anagram = True
        if len(word)==len(word3):
            for ch in word:
                dict1[ch]=word.count(ch)
                dict2[ch]=word3.count(ch)
            if dict1 != dict2 or word==word3: is_anagram=False
            if is_anagram == True: result.append(word2)
    return result
