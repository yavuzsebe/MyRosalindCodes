n=21
k=7
j=1
for i in range(n-k+1,n+1):
    j*=i
print(j%1000000)