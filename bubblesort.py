def bubbleSort(arr):
    for i in range (len(arr)):
        swapped = False
        for j in (range(0, len(arr)-i-1)):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
        
    return arr

print(bubbleSort([1,9,6,3]))
          