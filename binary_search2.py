
def binary_search(nums, n):
    low = 0 
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


a = [i for i in range(20)]
b = [i for i in range(40)]
c = [i for i in range(80)]

binary_search(c, 4)