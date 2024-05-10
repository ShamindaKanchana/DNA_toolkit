from DNAToolkit import*
from utilities import colored
import random
rnDNAStr="ATTTtttaaaaaatttttttttttccccccccccccccccgCGT"

''''
if(validateseq(rnDNAStr)):
    print("This is valid DNA sequence")
    print(validateseq(rnDNAStr))
else:
    print("This is not valid sequence") 

'''    

#creating a random DNA sequence for testing:
randDNAstr=''.join([random.choice(Nucleotides) 
                    for nuc in range(2000)])

randomBinary=''.join([random.choice(Binary)
                      for B in range(2000)])
'''
#To print random sequence after validating
print("--------------------Validated sequence is ----------------------------------------")
print((validateseq(randDNAstr)))
print(countNucFrequency(randDNAstr))

#To print trascript 
print("--------------------Transcripted DNA is ----------------------------------------")
print(transcription(randDNAstr))

print("\n\nGC content is   "+str(gc_content(randDNAstr)))

#Reverse complement
print("---------------------Reverse complement of  DNA is -----------------------------")
print(reverse_complement(randDNAstr));


#reverse sequence count
print(countNucFrequency(reverse_complement(randDNAstr)))

#DNA architecture
DNA_acr(randDNAstr)



'''

# Encode binary string to DNA sequence
binary_string=randomBinary
print("....................................Binary code .............................\n"+binary_string)
dna_sequence = encode_to_dna(binary_string)
print("\n........................Encoded DNA sequence...............................\n", dna_sequence)

# Decode DNA sequence to binary string
decoded_binary_string = decode_to_binary(encode_to_dna(binary_string), DNA_encode)
print("Decoded binary string......................................................\n", decoded_binary_string)