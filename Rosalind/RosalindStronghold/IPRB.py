k, m, n= 2, 2, 2
totIndv=k+m+n
poam=totIndv*(totIndv-1)*2 #production of all matings

populationProfiles=[]
populationProfiles+=[(1,1)]*k
populationProfiles+=[(1,0)]*m
populationProfiles+=[(0,0)]*n

domProfiles=[(1,0),(0,1),(1,1)]
recProfiles=[(0,0)]

osp=[] #offspring profiles

i=0
while i<(len(populationProfiles)):
    j=0
    while j<(len(populationProfiles)):
        if i!=j:
            k=0
            while k<2:
                l=0
                while l<2: 
                    osp+=[(populationProfiles[i][k],populationProfiles[j][l])]
                    l+=1
                k+=1
        else: 
            pass
        j+=1
    i+=1

domCount=0
recCount=0
for i in osp:
    if i in domProfiles:
        domCount+=1
    elif i in recProfiles:
        recCount+=1
if domCount+recCount==len(osp):
    print(domCount/len(osp))
else:
    print("There's been a mistake!")