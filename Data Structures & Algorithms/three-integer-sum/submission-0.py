class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for k, target in enumerate(nums):
            seen = set()
            for i in range(k+1, len(nums)):
                val = (target + nums[i]) * -1
                if val in seen:
                    res.append([target, nums[i], val])

                seen.add(nums[i])
        
        res = set(tuple(sorted(triplet)) for triplet in res)
        return list(res)
            
            