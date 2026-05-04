class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res : list[int] = [1 for x in range(len(nums))]

        for idx in range(1, len(nums)):
            res[idx] = res[idx-1] * nums[idx-1]

        suffice_prod_at_i = 1 # right o
        for idx in range(len(nums) -2, -1, -1):
            suffice_prod_at_i *=nums[idx + 1]
            res[idx] *= suffice_prod_at_i

        return res

        