with open("/Users/yavuzsebe/Downloads/rosalind_ddeg.txt","r") as inputSet:   #sample output: 2 4 2 2 2 2
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

graphDict={}
for i in range(vertices):
    if i+1 not in graphDict.keys():
        graphDict[i+1]=[]

for i in edgeList:
    graphDict[int(i.split()[0])]+=[int(i.split()[1])]
    graphDict[int(i.split()[1])]+=[int(i.split()[0])]

ddeg=[]
for i in range(vertices):
    ddeg+=[0]

for i in graphDict:
    for j in graphDict[i]:
        ddeg[i-1]+=len(graphDict[j])

ddegString=""
for i in ddeg:
    ddegString+=str(i)+" "

print(ddegString)