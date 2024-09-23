with open('/Users/yavuzsebe/Downloads/rosalind_lcsm.txt', 'r') as inputfasta:
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