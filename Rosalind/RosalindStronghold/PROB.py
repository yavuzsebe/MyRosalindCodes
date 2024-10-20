with open('/Users/yavuzsebe/Downloads/rosalind_prob.txt', 'r') as inputFile:
    inputLines=[]
    for line in inputFile:
        line = line.strip()
        inputLines.append(line)
    sequence=inputLines[0]
    arrayA=[]
    for k in inputLines[1].split():
        arrayA.append(k)
import math
arrayB=[]
for i in arrayA:
    i=float(i)
    probGorC=i/2
    probAorT=(1-i)/2
    prob=1
    for j in sequence:
        if j=="A" or j=="T":
            prob*=probAorT
        elif j=="G" or j=="C":
            prob*=probGorC
    arrayB.append(math.log(prob,10))
answerStr=""
for i in arrayB:
    answerStr+=str(i)+" "
print(answerStr)