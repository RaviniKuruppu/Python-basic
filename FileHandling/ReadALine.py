# write a program to read the n th line of a file
def readline(n):
    with open("ABC.txt","r")as file:
        a=0
        for line in file.readlines():
            a+=1
            
            if(a==2):
                print(line)
                break;
readline(2)