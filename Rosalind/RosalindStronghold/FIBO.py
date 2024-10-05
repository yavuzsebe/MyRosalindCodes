with open("/Users/yavuzsebe/Downloads/rosalind_fibo.txt","r") as inputFn:
    inputFn=int(inputFn.readlines()[0])
    l=[0,1,1]
i=0
while len(l)<=inputFn:
    l.append(l[-1]+l[-2])
    i+1
print(l[-1])