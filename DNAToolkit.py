Nucleotides=["A","C","G","T"]

#check the sequence to make sure it is a DNA string 
def validateseq(dna_seq):
    tmpseq=dna_seq.upper()
    for nuc  in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq    