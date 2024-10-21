from Bio import Entrez, SeqIO
import ssl

ssl._create_default_https_context=ssl._create_unverified_context
Entrez.email="xxx"

with open("/Users/yavuzsebe/Downloads/rosalind_frmt.txt","r") as inputFileRaw:
    inputFile,inputList=inputFileRaw.readlines(),[]
    for i in inputFile[0].split():
        inputList.append(i)

handle=Entrez.efetch(db="nucleotide",id=inputList,rettype="fasta")
records=list(SeqIO.parse(handle, "fasta"))

lenghts,i=[],0
while i<len(records):
    lenghts.append(len(records[i].seq))
    i+=1

description=records[lenghts.index(min(lenghts))].description
seq=records[lenghts.index(min(lenghts))].seq

fastaSeq,i="",0
while i<len(seq):
    if i%80==0:
      fastaSeq+="\n"
    fastaSeq+=seq[i]
    i+=1

print(f">{description}{fastaSeq}")