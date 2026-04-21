class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i,val in enumerate(nums):
            res = target - val
            if res in diff:
                return [diff[res], i]
            else:
                diff[val] = i