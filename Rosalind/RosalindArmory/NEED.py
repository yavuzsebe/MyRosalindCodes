from Bio import Entrez
import ssl, subprocess
ssl._create_default_https_context=ssl._create_unverified_context
Entrez.email="xxx"

idList=[]
with open("/Users/yavuzsebe/Downloads/rosalind_need.txt","r") as inputFileRaw: 
    #rosalind_need.txt contains "JX205496.1 JX469991.1" text.
    inputFile=inputFileRaw.readlines()
    idList.append(inputFile[0].split()[0])
    idList.append(inputFile[0].split()[1])
    #current idList should be ['JX205496.1', 'JX469991.1'].

fileOutput=[]
for i in idList:
    handle=Entrez.efetch(db="nucleotide",id=i,rettype="fasta")
    record=handle.read()
    fileOutput.append(record)

for i,j in zip(fileOutput,idList):
    with open(f"/Users/yavuzsebe/Downloads/data/{j}.fasta","w") as outputFasta:
        outputFasta.write(i)

subprocess.run(["needle", 
                f"/Users/yavuzsebe/Downloads/data/{idList[0]}.fasta", 
                f"/Users/yavuzsebe/Downloads/data/{idList[1]}.fasta",
                "-gapopen", "10",
                "-gapextend", "1",
                "-endopen", "10",
                "-endextend", "1",
                "-endweight",
                "-outfile",
                f"/Users/yavuzsebe/Downloads/data/output-{idList[0]}-{idList[1]}.txt"
                ])

with open(f"/Users/yavuzsebe/Downloads/data/output-{idList[0]}-{idList[1]}.txt","r") as output:
    outputReads=output.readlines()
    outputReadsStr=""
    for i in outputReads:
        outputReadsStr+=i

print(outputReadsStr[outputReadsStr.find("Score: "):outputReadsStr.find("\n", outputReadsStr.find("Score: "))])