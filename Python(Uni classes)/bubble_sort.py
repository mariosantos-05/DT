def bubble(arr):
    for num in range(len(arr)-1,0,1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                aux = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = aux