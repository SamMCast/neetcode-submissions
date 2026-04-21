class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        bit = [0] * 32
        for num in nums:
            for i in range(32):
                bit[i] += ((num >> i) & 1)

        res = 0
        for i in range(32):
            if bit[i] > (n // 2):
                    res |= (1 << i)
                    
        if bit[31] == 1:
            res -= (1 <<32)

        return res
        