from ast import arg


def quicksort(arr, low, high):
   if low < high: # Only sort if the subarray has more than one element, that is, when it is in the smallest subarray 
      # Partition the array and get the pivot index
      pivot_index = partition(arr,low,high)
      
      #Recursively sort the subarrays
      quicksort(arr, low, pivot_index - 1) # Left Part
      quicksort(arr, pivot_index + 1, high) # Right Part


# Divides the array in subregions
def partition(arr, low, high):
   
   #Choose the last element as the pivot
   pivot = arr[high]

   i = low -1 # Pointer to the smaller element

   #Loop through element to rearrange
   for j in range(low, high):
    if arr[j] <= pivot: # If the element is smaller than or equal to pivot
            i += 1      # Move the pointer for "smaller region" forward
            arr[i], arr[j] = arr[j], arr[i] # Swap elements

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 # Return the pivot's index


arr_1 = [10,7,8,9,1,5]

quicksort(arr_1, 0, 5)


# The worst implementation.
def quicksort_1(arr):
    if (len(arr) <= 2):
        return arr
    else:
        pivo = arr[0] #O pivô pode ser qualquer elemento presente no array. No quicksort prezamos por bons pivôs
        
        menores = [i for i in arr[1:] if i <= pivo] #Levamos em conta da segunda posição a diante já que o pivô é o primeiro elemento, então sem necessidade de percorrermos novamente.
        
        maiores = [i for i in arr[1:] if i > pivo]
        
    return quicksort_1(menores) + [pivo] + quicksort_1(maiores)


print(quicksort_1([1,2,3,4,5,6,7,8]))

