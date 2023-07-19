def primeFactor(x):
    i=2
    factors=[]
    while(x!=1):
        if(x%i==0):
            factors.append(i)
            x//=i
            i-=1
        
        i+=1
    return factors
p=3
current =1
list=[]
while(len(list)<p):
    prime =set(primeFactor(current))
    if (len(prime)==p):
        list.append(current)
    else:
        list=[]
    current+=1
print(list)
    
    