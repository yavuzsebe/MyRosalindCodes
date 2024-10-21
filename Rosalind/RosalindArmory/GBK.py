from Bio import Entrez
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
Entrez.email="xxx"

with open("/Users/yavuzsebe/Downloads/rosalind_gbk.txt","r") as inputFileRaw:
    inputFile=inputFileRaw.readlines()
    organism=inputFile[0].strip()
    mindate=inputFile[1].strip()
    maxdate=inputFile[2].strip()
handle=Entrez.esearch(db="nucleotide",term=f'"{organism}"[Organism] AND ("{mindate}"[PDAT]:"{maxdate}"[PDAT])')
record=Entrez.read(handle)
record["Count"]