from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numfreq = defaultdict(int)
        res = []
        for n in nums:
            numfreq[n]+=1
        
        for num, freq in numfreq.items():
            heapq.heappush(res,[freq, num])
            if len(res) > k:
                heapq.heappop(res)
        
        result = [row[1] for row in res]
        return result