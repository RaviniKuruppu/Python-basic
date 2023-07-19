def redact(variable):
    words = ["Mary", "Mallon"]
    if (variable in words): 
        return True
    else:
        return False
text = ["Mary", "Mallon","The", "most", "famous", "patient", "zero", "of","Mary", "Mallon"]

filtered = filter(redact, text)

print("Original text:",text)
print()

for s in text:
    print(s,end=" ")

print("Filtered text:")
for s in filtered:
    print(s)