with open("/Users/yavuzsebe/Downloads/rosalind_bfil.txt","r") as inputFileRaw:
    inputFile=inputFileRaw.readlines()
cutoff=int(inputFile.pop(0).split()[0])

with open("/Users/yavuzsebe/Downloads/rosalind_bfil_main.txt","w") as outputFile:
	for i in inputFile:
		outputFile.write(i)

inputList=[]
for i in inputFile:
    inputList.append(i.split())
        
for i in range(3,len(inputList),4):
    for j in range(0,len(inputList[i][0])):
        baseQuality=ord(inputList[i][0][j])-33
        if baseQuality<cutoff:
            inputList[i-2][0]=inputList[i-2][0][1:]
            inputList[i][0]=inputList[i][0][1:]
        else:
            break

for i in range(3,len(inputList),4):
    for j in range(len(inputList[i][0])-1,0,-1):
        baseQuality=ord(inputList[i][0][j])-33
        if baseQuality<cutoff:
            inputList[i-2][0]=inputList[i-2][0][:-1]
            inputList[i][0]=inputList[i][0][:-1]
        else:
            break

with open("/Users/yavuzsebe/Downloads/rosalind_bfil_answer.txt","w") as outputFile:
    spaceCount=0
    for i in inputList:
        if spaceCount%4!=0:
            outputFile.write(i[0]+"\n")
            spaceCount+=1
        elif spaceCount%4==0 and spaceCount!=0:
            outputFile.write("\n"+i[0]+"\n")
            spaceCount+=1
        else:
            outputFile.write(i[0]+"\n")
            spaceCount+=1