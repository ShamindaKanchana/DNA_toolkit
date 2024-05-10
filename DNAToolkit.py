import collections
from structures import*

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
    ''''DNA -> RNA Transcription replacing Thymine with Uracil'''
    return seq.replace("T","U")

def reverse_complement(seq):
    '''Swapping adenine with thymine and guanine with cytosine and reversing newly generated string'''
    return ''.join([DNA_reverse_Comp[nuc] for nuc in seq])[::-1]

def DNA_acr(seq):


    reverse=reverse_complement(seq)
    print("\n\n"+seq)
    print(''.join(['|' for c in range (len(seq))]))
    print(reverse)

def gc_content(seq):
    '''GC content in a DNA/RNA sequence'''
    return round((seq.count('C')+seq.count('G'))/len(seq)*100)    