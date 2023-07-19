def gcd(x,y):
    if y==0:
        return x 
    else:
        tmp=y 
        y=x%y 
        x=tmp
        return gcd(x,y)
print(gcd(10, 8))