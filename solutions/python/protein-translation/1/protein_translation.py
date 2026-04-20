codon_table = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
    "STOP": ["UAA", "UAG", "UGA"]
}
def proteins(strand):
    result=[]
    for i in range(0,len(strand),3):
        if strand[i:i+3] in codon_table["STOP"]:
            return result
        for key,value in codon_table.items():
            if strand[i:i+3] in value:
                result.append(key)
    return result 
