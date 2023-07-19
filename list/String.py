
# write a program to count the number of strings where the string length is 2 or more 
#and the first and last character are same from a given list of strings


name=['nimal','piyal','sunil','nipun']
count=0


print("first character ",name[0])
print("last character",name[len(name)-1])
for x in name:
    if (len(x)>2) :
        if(x[0]==x[len(x)-1]):
            count=count+1
print(count)
print()
# Sort the names    
print(name)
name.sort()
print(name)

