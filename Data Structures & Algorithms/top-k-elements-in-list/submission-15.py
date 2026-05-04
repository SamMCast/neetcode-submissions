from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq_buckets : list(list(int)) = [[] for bucket in range(len(nums)+1)]

        for num, freq in counts.items():
            freq_buckets[freq].append(num)
        
        res = []
        for freq in range(len(freq_buckets)-1, -1, -1):
            bucket = freq_buckets[freq]
            if bucket:
                res.extend(bucket)
            if len(res) >k:
                break
        
        return res[:k]