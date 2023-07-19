with open("79.txt","r")as F:
    line=F.readlines()

myList=[]
for x in range(50):
    line[x]=line[x].replace("\n","")
    #line[x]=int(line[x].replace("\n",""))
myList2=[]
print(line)
for i in line:
    x=0
    for num in i:
        myList[x]=num
        x+=1
        if(x==2):
            myList2.append(myList)
            myList=[]
            
print(myList2)



            
    


