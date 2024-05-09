from DNAToolkit import*
import random
rnDNAStr="ATTTtttaaaaaatttttttttttccccccccccccccccgCGT"


if(validateseq(rnDNAStr)):
    print("This is valid DNA sequence")
    print(validateseq(rnDNAStr))
else:
    print("This is not valid sequence") 

#creating a random DNA sequence for testing:
randDNAstr=''.join([random.choice(Nucleotides) 
                    for nuc in range(100)])

print(validateseq(randDNAstr))
print(countNucFrequency(randDNAstr))