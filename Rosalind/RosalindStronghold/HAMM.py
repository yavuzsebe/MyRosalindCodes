sampleDataset=open("/Users/yavuzsebe/Downloads/rosalind_hamm.txt","r")
datasetList=list(sampleDataset.readlines())
mainString=datasetList[0]
compareString=datasetList[1]
if len(mainString)==len(compareString):
    i=0
    j=0
    while i<len(mainString):
        if mainString[i]!=compareString[i]:
            j+=1
        i+=1
    print(j)
else: 
    print("String sizes doesn't match.")