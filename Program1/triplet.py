for a in range(1,1000):
    for b in range(1,1000):
        if(a+b>1000-a-b):
            c=1000-a-b
            if((a*a+b*b)==c*c):
                print("a",a)
                print("b",b)
                print("c",c)
                break;