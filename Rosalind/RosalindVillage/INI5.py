f = open("rosalind_ini5.txt" , "r")
g = open("output.txt" , "w")

list1=list(f.readlines())

a = 1

try: 

    for i in list1:

        g.write(list1[a])
        a+=2

except IndexError:

    g = open("output.txt","r")
    g.readlines()

g = open("output.txt","r")
g.readlines()