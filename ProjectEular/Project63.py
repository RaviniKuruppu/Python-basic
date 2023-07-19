count=0
for x in range(1,10):
    for n in range(1,100):
        y =x**n
        z =str(y)
        if (len(z)==n):
            count+=1
            #print(y)
print()
print(count)
        