num =int(input("Enter number"))
    
r=bin(num) # convert the number to binary form using a function
print(r)
 
 
 
# convert the number to binary form manualy
value="" 
v=int(input("Enter number"))
while(v!=0):
    
    reminder=v%2
    v//=2
    value=str(reminder) + value
print(value)    
