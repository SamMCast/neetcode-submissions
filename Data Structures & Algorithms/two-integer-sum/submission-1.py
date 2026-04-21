class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, op in enumerate(nums):
            diff = target - op
            if diff in numDict:
                return [numDict[diff], i]
            numDict[op] = i
