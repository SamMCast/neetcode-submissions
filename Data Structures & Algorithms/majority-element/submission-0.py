from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = Counter(nums)
        return res.most_common(1)[0][0]
         