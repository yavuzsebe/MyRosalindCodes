with open('/Users/yavuzsebe/Downloads/rosalind_lexv.txt','r') as inputFileRaw:
    inputFile=inputFileRaw.readlines()
    alphabet=inputFile[0].strip().split()
    n=int(inputFile[1])

result=[]

def generateStrings(alphabet,currentString,maxLength):
    if len(currentString)>0:
        result.append(currentString) 
    if len(currentString)==maxLength:
        return
    
    for char in alphabet:
        generateStrings(alphabet,currentString+char,maxLength)

generateStrings(alphabet,"",n)

for string in result:
    print(string)