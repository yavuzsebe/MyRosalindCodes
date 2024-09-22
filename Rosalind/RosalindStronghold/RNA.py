strvar=input("Input DNA sequence: ")
strlist=[]
empty_delimeter=""
def change(strvar):
    i=0
    while i<len(strvar):
        if strvar[i]=="T":
            strlist.append("A")
        elif strvar[i]=="A":
            strlist.append("T")
        elif strvar[i]=="G":
            strlist.append("C")
        elif strvar[i]=="C":
            strlist.append("G")
        else:
            strlist.append("x")
        i+=1
def merge(strlist):
    strlist.reverse()
    strlist=empty_delimeter.join(strlist)
    print(strlist)
#AAAACCCGGT
change(strvar)
merge(strlist)