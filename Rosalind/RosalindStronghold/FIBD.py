aliveCount=81
lifespan=18

children=[]
adults=[]
gdnm=[]
totalPairs=[]

s=0
while s<aliveCount:
    children+={0}
    adults+={0}
    gdnm+={0}
    totalPairs+={0}
    s+=1

children[0]+=1

m=1
n=0
while m<aliveCount:
    adults[m]-=gdnm[m-1]
    children[m]+=adults[m-1]
    adults[m]+=children[m-1]+adults[m-1]
    if m>lifespan-2:
        gdnm[m]=children[n]
        n+=1
    m+=1
print(adults[-1]+children[-1])