from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = defaultdict(int)
        for num in nums:
            if numCount[num] > 0:
                return True
            numCount[num]+=1

        return False
