from math import sqrt
numberCount =0
def isPrime(n):
    for x in range(2,int(sqrt(n)+1)):
        if(n%x==0):
            return False
    return True
    
for x in range(1,100001,2):
    if (isPrime(x)):
        numberCount+=1
        if(numberCount==10001):
            print(x)
            break
    
