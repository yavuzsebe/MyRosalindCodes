string1=list(input("string: "))
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=int(input("d: "))
string2= " "
string3= " "
while a<(b+1): 
    string2=string2+string1[a]
    a+=1
while c<(d+1): 
    string3=string3+string1[c]
    c+=1
else:
    print(string2+string3)