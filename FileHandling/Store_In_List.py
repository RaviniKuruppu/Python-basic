mylist=[]
with open("ABC.txt","r")as file:
    for line in file.readlines():
        print(line)
        mylist.append(line) 
print(mylist)
