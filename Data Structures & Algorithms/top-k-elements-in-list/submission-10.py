from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        K_freq_elements = []
        for num, freq in count.items():
            heapq.heappush(K_freq_elements, (freq, num))
            if len(K_freq_elements) > k:
                heapq.heappop(K_freq_elements)
            

        return [item[1] for item in K_freq_elements]
            