def twoSum(nums: list[int], target: int) -> list[int]:
    hash_num = {}
    
    for i, num in enumerate(nums):
        
        complement = target - num
        
        if complement in hash_num:
            return [hash_num[complement], i]
        
        hash_num[num] = i
    
        
res = twoSum([2,7,11,15], 9)
#res2 = twoSum([3,2,4], 6)
print(res)
#print(res2)