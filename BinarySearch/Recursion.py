# Check whether the number is in the list
def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        mid = len(a_list) // 2
    if a_list[mid] == item:
        return True
    else:
        if item < a_list[mid]:
            return binary_search_rec(a_list[:mid], item)
        else:
            return binary_search_rec(a_list[mid + 1:], item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search_rec(test_list, 7))
    