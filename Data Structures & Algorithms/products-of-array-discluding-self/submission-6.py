class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res : list[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        suffix_product_at_j = 1
        for j in range(len(nums) -1, -1, -1):
            res[j] *= suffix_product_at_j
            suffix_product_at_j *= nums[j]

        return res