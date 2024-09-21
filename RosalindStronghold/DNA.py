strvar=input("Input DNA string: ")
strlist=[]
i=0
while i<len(strvar):
    strlist.append(strvar[i])
    i+=1
dict1={}
for word in strlist:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1
print(dict1)
print(dict1["A"], dict1["C"], dict1["G"], dict1["T"])