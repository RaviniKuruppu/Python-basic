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



# Convert a string to char list
t="nagaram"
char_list = list(t)
print(char_list)

#check if a element is present in string
if("a" in t):
    print("a is in the string") 

#iterate through a string
for i in t:
    print(i)