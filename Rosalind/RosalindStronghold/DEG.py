with open("/Users/yavuzsebe/Downloads/rosalind_deg.txt","r") as inputSet:   #sample output: 2 4 2 2 2 2
    inputSet=inputSet.readlines()
    i=0
    while i<len(inputSet)-1:
        inputSet[i]=inputSet[i][0:-1]
        i+=1
    i=1


edgeList=[]
while i<len(inputSet):
    edgeList.append(inputSet[i])
    i+=1

splitList=[]
for i in edgeList:
    splitList.append(i.split())


mentionCount=[]
for j in splitList:
    for k in j:
        if k!=" ":
            mentionCount+=[int(k)]
        else:
            pass
        
vertices=int(inputSet[0].split()[0])
degrees=[]
i=0
while i<vertices:
    degrees+=[0]
    i+=1   

for i in mentionCount:
    degrees[i-1]+=1
degreesString=""

for i in degrees:
    degreesString+=str(i)+" "  
print(degreesString)