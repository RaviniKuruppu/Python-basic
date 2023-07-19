

tot=0
first,second=1,2
while(second<=4000000):  
    if (second%2==0):
            tot+=second
            #print(tot)
    first,second=second,first+second
            
print(tot)       