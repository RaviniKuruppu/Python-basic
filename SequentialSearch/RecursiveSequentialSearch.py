## Check whether the number is in the list
def sequential_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    elif a_list[0] == item:
        return True
    else:
        return sequential_search_rec(a_list[1:], item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(sequential_search_rec(test_list, 3))
