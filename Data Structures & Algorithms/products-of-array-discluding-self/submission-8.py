class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for idx in range(1, len(nums)):
            res[idx] = res[idx -1] * nums[idx-1]

        product_after_j_idx = 1
        for j_idx in range(len(nums)-1, -1, -1):
            res[j_idx] *= product_after_j_idx
            product_after_j_idx *= nums[j_idx]
    
        return res