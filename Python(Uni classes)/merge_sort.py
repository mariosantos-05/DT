def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]

        mergeSort(l)
        mergeSort(r)

        i=0
        j=0
        k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k]=l[i]
                i=i+1
            else:
                arr[k]=r[j]
                j=j+1
            k=k+1

        while i < len(l):
            arr[k]=l[i]
            i=i+1
            k=k+1

        while j < len(r):
            arr[k]=r[j]
            j=j+1
            k=k+1