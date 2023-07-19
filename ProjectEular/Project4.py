
def test(m):
    l =len(string)
    for i in range(0,l):
        number = string[i:]+string[:i]
        print(number)
        if(string==number):
            palindrome= m
            return True
        
     
     
largestPalindrome=1    
for x in range(100,1000):
    for y in range(x+1,10000):
        m=x*y
        string=str(m)
if(test(m)):
    if(largestPalindrome<m):
        largestPalindrome= m
print(largestPalindrome)
    

    