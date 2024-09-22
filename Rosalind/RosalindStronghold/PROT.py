codonTable={
    "AUG":["M"],
    "UAA":["Stop"],"UAG":["Stop"],"UGA":["Stop"],
    "UUU":["F"],"UUC":["F"],
    "UUA":["L"],"UUG":["L"],"CUU":["L"],"CUC":["L"],"CUA":["L"],"CUG":["L"],
    "UCU":["S"],"UCC":["S"],"UCA":["S"],"UCG":["S"],"AGU":["S"],"AGC":["S"],
    "UAU":["Y"],"UAC":["Y"],
    "UGU":["C"],"UGC":["C"],
    "UGG":["W"],
    "CCU":["P"],"CCC":["P"],"CCA":["P"],"CCG":["P"],
    "CAU":["H"],"CAC":["H"],
    "CAA":["Q"],"CAG":["Q"],
    "CGU":["R"],"CGC":["R"],"CGA":["R"],"CGG":["R"],"AGA":["R"],"AGG":["R"],
    "AUU":["I"],"AUC":["I"],"AUA":["I"],
    "ACU":["T"],"ACC":["T"],"ACA":["T"],"ACG":["T"],
    "AAU":["N"],"AAC":["N"],
    "AAA":["K"],"AAG":["K"],
    "GUU":["V"],"GUC":["V"],"GUA":["V"],"GUG":["V"],
    "GCU":["A"],"GCA":["A"],"GCC":["A"],"GCG":["A"],
    "GAU":["D"],"GAC":["D"],
    "GAA":["E"],"GAG":["E"],
    "GGU":["G"],"GGC":["G"],"GGA":["G"],"GGG":["G"],
}
dnaStringFile=open("/Users/yavuzsebe/Downloads/rosalind_prot.txt","r")
dnaString=str(dnaStringFile.readlines())   
dnaString=dnaString[2:-4]
i=0
stopCodons=["UAA","UAG","UGA"]
proteinString=" "
while i<len(dnaString):
    if dnaString[i:i+3] in stopCodons:
        break
    if dnaString[i:i+3] in list(codonTable.keys()):
        proteinString=proteinString+str(list(codonTable.values())[list(codonTable.keys()).index(dnaString[i:i+3])])
    i+=3
    proteinString=proteinString.replace("['","")
    proteinString=proteinString.replace("']","")
print(dnaString+"\n")
print(proteinString)