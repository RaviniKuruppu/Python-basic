x= 600851475143
y=2
max=0
while(x>2):
    if(x%y==0):
        if(max<y):
            max=y
        x=x/y
        #print(y)
    else:
        y=y+1
print(max)