

# - Time complexity:
#   - Best Case: O(n) <- Sorted array
#   - Worst/avarage Case: O(n²)  
# - Space complexity: O(1) <- Only change the order of the elements

def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n == 1:
        return arr
    
    for _ in range(len(arr) - 1):
        is_sorted = True
        for i in range(n -1):
            if arr[i] > arr[i+1]:
                is_sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if is_sorted:
            return arr
    return arr

print(bubble_sort([5,4,3,2,1]))