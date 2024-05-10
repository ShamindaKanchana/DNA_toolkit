Nucleotides=["A","C","G","T"]

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