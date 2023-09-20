def binary(arr, key):
    l = 0
    r =  len(arr)-1
    while (l <= r):
        mid = (l+2) // 2
        if mid > key:
            arr[r] = mid - 1
        elif mid < key:
            arr[l] = mid + 1
        else:
            return mid        