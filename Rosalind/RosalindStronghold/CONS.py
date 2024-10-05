with open('/Users/yavuzsebe/Downloads/rosalind_cons.txt', 'r') as inputfasta:
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

baseFreq={
    "A":[],
    "C":[],
    "G":[],
    "T":[]
}
for i in baseFreq : 
    for j in range(len(fastaFile[list(fastaFile.keys())[0]][0])):
        baseFreq[i]+=[0]

for i in fastaFile:
    for j in fastaFile[i]:
        m=0
        while m<len(j):
            if j[m]=="A":
                baseFreq["A"][m]+=1
            if j[m]=="T":
                baseFreq["T"][m]+=1
            if j[m]=="G":
                baseFreq["G"][m]+=1
            if j[m]=="C":
                baseFreq["C"][m]+=1
            m+=1
            
indexFreq={}
for i in range(len(baseFreq[list(baseFreq.keys())[0]])):
    indexFreq[str(i)]=[]

for i in range(len(list(baseFreq.values()))):
    j=0
    while j<len(list(baseFreq.values())[i]):
        indexFreq[str(j)]+=str(list(baseFreq.values())[i][j])
        j+=1

consensus=""
for i in indexFreq.keys():
    baseIndex=indexFreq[i].index(max(indexFreq[i]))
    if baseIndex==0:
        consensus+="A"
    elif baseIndex==1:
        consensus+="C"
    elif baseIndex==2:
        consensus+="G"
    elif baseIndex==3:
        consensus+="T"
print(consensus)

for i in baseFreq:
    n=0
    emptyLine=""
    while n<len(baseFreq[i]):
        emptyLine+=(str(baseFreq[i][n])+" ")
        n+=1
    print("{}: {}".format(i,emptyLine))