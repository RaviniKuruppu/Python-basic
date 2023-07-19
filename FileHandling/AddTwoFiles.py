# Method 1
mylist1=[]
mylist2=[]
with open("ABC.txt","r")as file:
    for line in file.readlines():
        mylist1.append(line) 
        
with open("ABCD.txt","r")as file:
    for line in file.readlines():
        mylist2.append(line) 


        
print(dict(zip(mylist1,mylist2)))        
with open("new.txt","w")as A:
    
    for i in range(6):
        A.write(mylist1[i].replace("\n"," "))
        A.write(mylist2[i])
        i+=1
f= open("new.txt","r")
print(f.read())
f.close()



#method 2
with open("ABC.txt")as F1,open("ABCD.txt")as F2 ,open("newFile",'w')as F3:
        for l1,l2 in zip(F1,F2):
            F3.write(l1.replace("\n"," ")+l2)
            print("job done")


