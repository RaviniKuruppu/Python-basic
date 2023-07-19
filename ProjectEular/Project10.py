from math import sqrt
numberSum =0
def isPrime(n):
    for x in range(2,int(sqrt(n)+1)):
        if(n%x==0):
            return False
    return True
    
for x in range(2,2000001):
    if (isPrime(x)):
        numberSum+=x
        
print(numberSum)