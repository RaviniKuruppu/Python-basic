total=0
list=[]
string=""
for i in range(6,11):
    for j  in reversed(range(5)):
        y=j+1
        for k in range(1,6):
            total =i+y+k
            if(total==14):
                string=i,y,k
                print(string)
           