num = input('Enter Number or Phrase:')
def ispalindrome(num):
    return str(num) == str(num)[::-1]
    return False
ispalindrome(num)

if ispalindrome(num) == True:
    print (str(num) + ' is palindromic')
else:
    print (str(num) + ' is not palindromic')