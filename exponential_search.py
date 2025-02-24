
# O(log n)
 
def binary_search(nums, n, low, high):
    high = len(nums)
    steps = 0
    while low < high:
        steps += 1
        mid  = int((low + high) / 2)
        
        if nums[mid] == n:
            print("steps:", steps)
            return mid
        elif nums[mid] < n:
            low = mid + 1
        else: 
            high = mid
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    
    while i < n and arr[i] < target:
        i *= 2
        
    if arr[i] == target:
        return i
    
    return binary_search(arr, target, i // 2, min(i,n-1) ) # The index can be out of bounds


arr = [i for i in range(10000)]

print(exponential_search(arr, 2))