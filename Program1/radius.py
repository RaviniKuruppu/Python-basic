import math;
R=int(input("Enter radius"))
temparea,area,width =0,0,0
for x in range(1,2*R):
    temparea=x*(2*math.sqrt(R**2-(x**2)/4))
    print(temparea)
    if(area<temparea):
        area=temparea
        width=x
        heigth=(2*math.sqrt(R**2-(x**2)/4))
    else:
        print("Maximum area ",area)
        print("Maximum width ",width)
        print("Maximum heigth ",heigth)  
        break;