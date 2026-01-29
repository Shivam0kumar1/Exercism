import string
def to_rna(dna_strand):
    """Version 1"""
    # DNA_NUCLEOTIDE = "GCTA"
    # RNA_NUCLEOTIDE = "CGAU"
    # NUCLEOTIDE_COMPLEMENT = str.maketrans(DNA_NUCLEOTIDE,RNA_NUCLEOTIDE)
    # return dna_strand.translate(NUCLEOTIDE_COMPLEMENT)

    """Version 2"""
    NUCLEOTIDE_COMPLEMENT = {"G":"C","C":"G","T":"A","A":"U"}
    rna_complement = ""
    for ch in dna_strand:
        rna_complement+=NUCLEOTIDE_COMPLEMENT[ch]
    return rna_complement
        