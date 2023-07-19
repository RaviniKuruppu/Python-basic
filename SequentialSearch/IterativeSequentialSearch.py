# Iterative Sequential Search
def sequential_search(a_list, item):
    pos = 0
    found = False
    
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    if found:
        return pos
    else:
        return -1

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(sequential_search(test_list, 13))