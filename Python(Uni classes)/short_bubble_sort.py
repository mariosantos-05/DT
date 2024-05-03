def short_bubble(arr):
    exchanges = True
    num = len(arr)-1
    while num > 0  and exchanges:
        exchanges = false
        for i in range(num):
            if arr[i] > arr[i+1]:
                exchanges = False
                aux = arr[i]
                arr[i+1] = aux
    num = num - 1            