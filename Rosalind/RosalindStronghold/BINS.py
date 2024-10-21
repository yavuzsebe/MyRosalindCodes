with open('/Users/yavuzsebe/Downloads/rosalind_bins.txt', 'r') as inputBins:
    inputBins=inputBins.readlines()

array=[]
for i in inputBins[2].split():
    array.append(int(i))

searchList=[]
for i in inputBins[3].split():
    searchList.append(int(i))

answer=[]
for i in searchList:
    start=0
    end=len(array) - 1    
    while start<=end:
        mid=(start+end)//2
        if array[mid] == i:
            answer.append(mid+1)
            break
        elif array[mid]<i:
            start=mid+1
        else:
            end=mid-1
    else:
        answer.append(-1)

answerStr=""
for i in answer:
    answerStr+=str(i)+" "
print(answerStr)