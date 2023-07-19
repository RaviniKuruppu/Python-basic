def longestword(n):
    y=0
    with open(n,"r")as A:
        list=A.read().split( )
        for x in list:
            if(len(x)>y):
                word=x
                y=len(x)
        print("longest word="+word)
longestword("ABC.txt")
        