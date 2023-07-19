list=["Ravini",45,1.9]
print(list[2])
print(list[-1]) # going from back
print(list[-2])


list=list+[12,13] # added to the end
print(list)

list[2:4]=[99,100] # values in 2 to 3 index are replaced by 99 and 100
print(list)
print()
list[2:2]=['A','B']
print(list)