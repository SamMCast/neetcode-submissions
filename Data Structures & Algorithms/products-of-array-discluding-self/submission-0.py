class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #let's try a brute force approach first
        prdArry = [0 for x in nums]
        for i in range(len(nums)):
            prd = 1
            j = (i+1) % len(nums)
            while j !=i:
                prd*= nums[j]
                j = (j+1) % len(nums)
            prdArry [i] = prd
        return prdArry

