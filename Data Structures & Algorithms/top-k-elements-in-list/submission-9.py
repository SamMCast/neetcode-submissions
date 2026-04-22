from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = counts.most_common(k)
        return [item[0] for item in res]
        
