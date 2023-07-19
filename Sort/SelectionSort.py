def selection_sort(a_list):
    # outer loop
    for j in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        # inner loop
        for i in range(1, j + 1):
            if a_list[i] > a_list[pos_of_max]:
                pos_of_max = i
                # do a swap
                temp = a_list[j]
                a_list[j] = a_list[pos_of_max]
                a_list[pos_of_max] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)
