def prot(dnaString):
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
    print(proteinString)

with open('/Users/yavuzsebe/Downloads/rosalind_splc.txt', 'r') as inputfasta:
    fasta_dictionary = {}
    fasta_header = ""
    for line in inputfasta:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            fasta_header = line[1:]
            if fasta_header not in fasta_dictionary:
                fasta_dictionary[fasta_header] = []
            continue
        sequence = line
        fasta_dictionary[fasta_header].append(sequence)
fastaFile={}
i=0
while i<len(list(fasta_dictionary.keys())):
    j=0
    emptyStr=""
    while j<len(fasta_dictionary[list(fasta_dictionary.keys())[i]]):
        a=[]
        a=list(list(fasta_dictionary[list(fasta_dictionary.keys())[i]]))[j]
        emptyStr=emptyStr+a
        j+=1
    fastaFile[list(fasta_dictionary.keys())[i]]=[]
    fastaFile[list(fasta_dictionary.keys())[i]].append(emptyStr)
    i+=1
mainSeq=str(fastaFile[list(fastaFile.keys())[0]])[2:-2]
i=1
while i <len(list(fastaFile.keys())):
    if str(fastaFile[list(fastaFile.keys())[i]])[2:-2] in mainSeq:
        mainSeq=mainSeq.replace(str(fastaFile[list(fastaFile.keys())[i]])[2:-2],"")
    i+=1
mainSeq=mainSeq.replace("T","U")
prot(mainSeq)