N=int(input("Enter perimeter"))
temparea,area,width =0,0,0
for x in range(1,N//2):
    temparea =x*((N-2*x)/2)
    if(area<temparea):
        area=temparea
        width=x
        heigth=(N-2*x)/2
    else:
        print("Maximum area ",area)
        print("Maximum width ",width)
        print("Maximum heigth ",heigth)  
        break;   