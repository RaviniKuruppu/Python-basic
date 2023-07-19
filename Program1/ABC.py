firstNumber,secondNumber,sum=1,2,2;
while(True):
    firstNumber,secondNumber= secondNumber,firstNumber+secondNumber;
    if(secondNumber>=4000000):
        break;
    if(secondNumber%2==0):
        sum+=secondNumber;
print(sum)