
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        possibles = []
        for num in nums:
                if num < target:
                    possibles.append(num)
        print(possibles)
        
        result = []
        
        max_number = list(max(possibles))

        integrate = list(filter(lambda x: x < max_number, possibles))

        result.append(integrate)
        result.append(max_number)

        print(result)


        
      
twoSum([3,4,5],9)