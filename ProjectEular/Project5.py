def test(x):
    for y in range(1,21):
        if(x%y!=0):
            return False
    return True

x=1
while(True):
    if(test(x)):
        break
    x+=1
    
print(x)