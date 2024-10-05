with open("/Users/yavuzsebe/Downloads/rosalind_bfs.txt","r") as inputSet:
    inputSet = inputSet.readlines()
    i = 0
    while i < len(inputSet) - 1:
        inputSet[i] = inputSet[i].strip()
        i += 1
    i = 1

root = 1
vertices = int(inputSet[0].split()[0])

edgeList = []
while i < len(inputSet):
    edgeList.append(inputSet[i])
    i += 1

splitList = []
for i in edgeList:
    splitList.append(i.split())

graphDict={}
for i in splitList:
    if int(i[0]) not in graphDict.keys():
        graphDict[int(i[0])]=[]
    if int(i[1]) not in graphDict[int(i[0])]:
        graphDict[int(i[0])]+=[int(i[1])]

Q=[root] 
V=set() 
distances=[-1]*vertices
distances[root-1]=0

while Q:
    current=Q.pop(0)
    V.add(current)

    if current in graphDict:
        for neighbor in graphDict[current]:
            if neighbor not in V and distances[neighbor-1]==-1:
                distances[neighbor-1] = distances[current-1]+1
                Q.append(neighbor)

answerStr=" ".join(map(str, distances))
print(answerStr)