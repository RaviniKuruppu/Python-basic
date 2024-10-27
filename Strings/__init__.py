#Convert a string to lower case and remove all non-alphanumeric characters.

def stringConvertion(s):
    s=s.lower()
    cleaned_chars = []
    for char in s:
        if char.isalpha():
            cleaned_chars.append(char)
    s = ''.join(cleaned_chars)
    return s
        
print(stringConvertion("A man, a plan, a canal: Panama"))

#Output-amanaplanacanalpanama