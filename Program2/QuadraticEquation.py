import math;
b = (int)(input("b value"))
a = (int)(input("a value"))
c =(int) (input("c value"))
b2_4ac=(b**2)-(4*a*c)
if(b2_4ac>0):
    sqrt_value=math.sqrt(b2_4ac)
    ans1=-b-sqrt_value
    ans2=-b+sqrt_value
    FinalAns1=ans1/(2*a)
    FinalAns2=ans2/(2*a)
    print("final ans1"=str(FinalAns1))
    print("final ans2"=str(FinalAns2))
else:
    print("invalid number")
  
