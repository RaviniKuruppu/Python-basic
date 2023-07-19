x=chr(ord("G")^32) # swapping
print(x)

y=chr(ord("G")|32)
print(y)


for char in 'Hello':
    print(chr(ord(char)^32),end='') # turn the case
print()    
for char in 'Hello':
    print(chr(ord(char)|32),end='') # turn to lower case