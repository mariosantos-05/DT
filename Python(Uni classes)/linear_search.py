def linear_search(arr, key):
    found = False
    i = 0
    while i < len(arr) and found == False:
        if arr[i] == key:
            found = True
        else:
            i+= 1
    return found            
