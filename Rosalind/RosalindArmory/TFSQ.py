with open("/Users/yavuzsebe/Downloads/rosalind_tfsq.txt","r") as inputFileRaw:
    inputFile=inputFileRaw.readlines()
    
answerStr,i="",0

while i<len(inputFile):
    id=inputFile[i].strip()[1:]
    seq=inputFile[i+1].strip()
    answerStr+=f">{id}\n{seq}\n"
    i+=4

with open("/Users/yavuzsebe/Downloads/answer.txt", "w") as file:
    file.write(answerStr)