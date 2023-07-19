from math import sqrt
def is_prime(n):
    for x in range(2,int(sqrt(n))+1):
        if(n%x==0):
            return False;
    return True;


def goldbatch():
    number =7;
    while(True):
        number+=2;
        for i in range(0,number):
            check = number-(i**2)*2
            if(check<0):
                print(" number ",number)
                return number;
            if(is_prime(check)):
                break;
            
            
            
            
            
            
''''def isPrime(n):
    for x in range(2,int(sqrt(n)+1)):
        if(n%x==0):
            return False
    return True
number=9

while (True):
    if(isPrime(number) or number%2==1):
        #print(number)
        number+=1 
        #continue
    t=1 
    x=number-(2*t*t)
    current=False   
    while(x)>0:
        if(isPrime(x)):
            #print(number)
            current=True
            break
        t+=1
    number+=1
       
    
    
    if(not current):
        print(number)
        break '''
    
            
