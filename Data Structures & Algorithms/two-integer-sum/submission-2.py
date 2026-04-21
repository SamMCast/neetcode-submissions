class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         #let's try an nlogn solution first
       
        lookup = {}
        for i,n in enumerate(nums):
            x = target - n
            if x in lookup:
                return [lookup[x], i]
            lookup[n] =i
        