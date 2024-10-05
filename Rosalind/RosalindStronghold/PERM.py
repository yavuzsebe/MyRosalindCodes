def product(x):
        final = [[]]
        l = len(x)
        groups = [list(x)] * l
        for i in groups:
            final = [x+[y]  for x in final  for y in i]
        for k in final:
                yield "".join(k)
with open("/Users/yavuzsebe/Downloads/rosalind_perm.txt","r") as permInput:
    permInput=permInput.readlines()
    permInput=int(permInput[0])
n=1
permTot=1
r=range(n,permInput+1)
for num in r:
    permTot*=num
print(permTot)
str1=""
for number in list(r):
    str1+=str(number)
list1=list(product(str1))
list2=[]
for el in list1:
    if len(set(list(el)))==len(el):
        print(el)