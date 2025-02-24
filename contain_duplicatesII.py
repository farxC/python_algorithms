
def containNearbyDuplicates(nums: list[int], k: int) -> bool:
    l, r = 0, 0# initialize two pointers for representing the window
    d = {}
    while r < len(nums) - 1:
        r += 1
        if nums[r] in d and abs(d.get(nums[r]) -r) <= k:
            return True
        else:
            d[nums[r]] = r
            
        if r - l > k:
            del d[nums[l]]
            l += 1
        print(l, r)              
        return False


# print(containNearbyDuplicates([1,2,3,1,2,3], 2)) #Expected false

# print(containNearbyDuplicates([1,2,3,1], 3))

print(containNearbyDuplicates([1,0,1,1], 1))