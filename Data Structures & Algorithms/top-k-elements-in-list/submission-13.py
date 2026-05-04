from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        counts = Counter(nums)

        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
        
        while len(min_heap) > k:
            heapq.heappop(min_heap)

        return [item[1] for item in min_heap]