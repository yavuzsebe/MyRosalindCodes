with open('/Users/yavuzsebe/Downloads/rosalind_iev.txt', 'r') as inputArray:
    couples=[]
    for line in inputArray:
        for couple in line.split():
            couples.append(float(couple))
answer=2*(1*couples[0]+1*couples[1]+1*couples[2]+0.75*couples[3]+0.5*couples[4]+0*couples[5])
print(answer)