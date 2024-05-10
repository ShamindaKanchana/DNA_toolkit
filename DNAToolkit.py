import collections
from structures import*

import binascii

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



def encode_to_dna(binary_string):
    # Ensure the length of the binary string is divisible by 2
    if len(binary_string) % 2 != 0:
        raise ValueError("Binary string length must be divisible by 2")

    dna_sequence = ""
    # Iterate over the binary string in chunks of 2
    for i in range(0, len(binary_string), 2):
        chunk = binary_string[i:i+2]
        # Convert the chunk to its corresponding DNA base
        dna_base = ''
        if chunk == '00':
            dna_base = 'A'
        elif chunk == '01':
            dna_base = 'G'
        elif chunk == '10':
            dna_base = 'T'
        elif chunk == '11':
            dna_base = 'C'
        dna_sequence += dna_base

    # Handle the last bit
    if len(binary_string) % 2 != 0:
        last_bit = int(binary_string[-1])
        if last_bit == 0:
            dna_sequence += 'A'
        else:
            dna_sequence += 'T'

    return dna_sequence

def decode_to_binary(dna_sequence, dna_encode):
    binary_string = ""
    # Iterate over the DNA sequence
    for base in dna_sequence:
        # Convert the DNA base to its corresponding binary chunk
        binary_chunk = dna_encode[base]
        binary_string += binary_chunk

    return binary_string




def text_to_binary(text):
    # Convert the text to bytes using UTF-8 encoding
    byte_string = text.encode('utf-8')
    # Convert the byte string to binary representation
    binary_string = bin(int.from_bytes(byte_string, 'big'))[2:]
    return binary_string

