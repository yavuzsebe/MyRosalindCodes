string1 = input("Input text: ")
dict1={}
strlist=string1.split(" ")
dict1={}
dict1=dict(dict1)
for key in strlist:
    if key in dict1:
        dict1[key]=dict1[key]+1
    else:
        dict1[key]=1
for keys, value in dict1.items():
    print(keys)
    print(value)