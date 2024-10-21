sampleDataset=open("/Users/yavuzsebe/Downloads/rosalind_subs.txt","r")
datasetList=list(sampleDataset.readlines())
dnaSequence=datasetList[0][0:-1]
motifSequence=datasetList[1][0:-1]
mL=len(motifSequence)
dL=len(dnaSequence)
subCons=dL-mL
i=0
ansList=[]
ansStr=""
while i<subCons:
    if dnaSequence[i:i+mL]==motifSequence:
        ansStr=ansStr+" "+str(i+1)
    else:
        pass
    i+=1
print(ansStr)