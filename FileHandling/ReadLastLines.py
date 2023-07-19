# read the last n lines.
def readline(n):
    with open("ABC.txt","r")as file:
        for line in file.readlines()[-n:]:
            print(line)             
                       
readline(3)