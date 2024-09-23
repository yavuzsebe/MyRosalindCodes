
codonTable={
    "M":["AUG"],
    "Stop":["UAA","UAG","UGA"],
    "F":["UUU","UUC"],
    "L":["UUA","UUG","CUU","CUC","CUA","CUG"],
    "S":["UCU","UCC","UCA","UCG","AGU","AGC"],
    "Y":["UAU","UAC"],
    "C":["UGU","UGC"],
    "W":["UGG"],
    "P":["CCU","CCC","CCA","CCG"],
    "H":["CAU","CAC"],
    "Q":["CAA","CAG"],
    "R":["CGU","CGC","CGA","CGG","AGA","AGG"],
    "I":["AUU","AUC","AUA"],
    "T":["ACU","ACC","ACA","ACG"],
    "N":["AAU","AAC"],
    "K":["AAA","AAG"],
    "V":["GUU","GUC","GUA","GUG"],
    "A":["GCU","GCA","GCC","GCG"],
    "D":["GAU","GAC"],
    "E":["GAA","GAG"],
    "G":["GGU","GGC","GGA","GGG"],
}
with open("/Users/yavuzsebe/Downloads/rosalind_MRNA.txt","r") as protSeq:
    protSeq=protSeq.readlines()
    protSeq=protSeq[0]
i=0
j=3
while i<len(protSeq):
    if protSeq[i] in codonTable.keys():
        j=j*len(codonTable[protSeq[i]])
    i+=1
print(j)
    