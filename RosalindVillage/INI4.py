x=int(input("x: "))
y=int(input("y: "))
a= list(range(x, y+1))
b=0
for i in a:
    if i%2==1:
        b+=i
    else:
        pass
print(b)