def partition(arr, low, high):
    # pick the last element in the array as pivot
    pivot = arr[high]
    # set the index of smaller element
    i = (low-1)
    for j in range(low, high):
        
        # If current element is smaller or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] # swap
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if low < high:
    # arr[pidx] will now be placed at the right place
        pidx = partition(arr,low,high)
    # Separately sort elements before and after partition
        quickSort(arr, low, pidx-1)
        quickSort(arr, pidx+1, high)
    
arr = [10, 5, 7, 9, 1, 3]
n = len(arr)
quickSort(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d " %arr[i], end = "")
