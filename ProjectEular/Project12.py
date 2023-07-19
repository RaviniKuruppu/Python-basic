# triangle number
def div(t):
    list=[]
    for j in range(1,t+1):
        if(t%j==0):
            list.append(j)
    #print(list)
    length=len(list) 
    #print(length)
    if (length>500):
        print("triangle number ",t) 
        return True
    return False



t=0
i=0
while(True):
    t=t+i
    #print(t)
    if(div(t)):
        break
    i=i+1
   



    
    