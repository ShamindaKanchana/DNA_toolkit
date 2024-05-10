Nucleotides=["A","C","G","T"]
DNA_reverse_Comp={"A":"G","G":"A","C":"T","T":"C"}
#check the sequence to make sure it is a DNA string 
def validateseq(dna_seq):
    tmpseq=dna_seq.upper()
    for nuc  in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq    

def countNucFrequency(seq):
    tmpFreqDict={"A":0,"C":0,"G":0,"T":0}
    for nuc in seq:
        tmpFreqDict[nuc]+=1
    return tmpFreqDict    

def transcription(seq):
    #DNA to RNA 
    return seq.replace("T","U")

def reverse_complement(seq):
    return ''.join([DNA_reverse_Comp[nuc] for nuc in seq])[::-1]

def DNA_acr(seq):
    reverse=reverse_complement(seq)
    print("\n\n"+seq)
    print(''.join(['|' for c in range (len(seq))]))
    print(reverse)