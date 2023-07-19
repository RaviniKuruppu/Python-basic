# read the first n lines
def readline(n):
    with open("ABC.txt","r")as file:
        a=0
        for line in file.readlines():
            a+=1
            print(line)
            if(a==n):
                break;
readline(3)