
#O(n^2) - Quadratic Time
def insertionSort(arr):
    
    for i in range(len(arr)):
        key = arr[i] # Actual element being transversed
        j = i - 1 # Reference to the index already sorted
        
        while j > 0 and arr[j] > key: # While loop when we aren't out of bounds and the "j" element is greater than the key
            arr[j + 1] = arr[j] # Switching J
            j = j - 1
        
        arr[j + 1] = key # Current i position
    return arr

print(insertionSort([2,3,4,10,9,5,11,15,12]))