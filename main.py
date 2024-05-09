from DNAToolkit import*
rnDNAStr="ATTTtttaaaaaatttttttttttccccccccccccccccgCGT"


if(validateseq(rnDNAStr)):
    print("This is valid DNA sequence")
    print(validateseq(rnDNAStr))
else:
    print("This is not valid sequence") 
