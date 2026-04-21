class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [nums[x % len(nums)] for x in range(len(nums)*2)]