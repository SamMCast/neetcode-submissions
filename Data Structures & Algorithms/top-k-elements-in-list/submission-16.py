from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        
        # Polish: Correct type hints and using '_' for unused variable
        freq_buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            freq_buckets[freq].append(num)
        
        res = []
        # Polish: Iterating backward using standard range
        for freq in range(len(freq_buckets) - 1, -1, -1):
            bucket = freq_buckets[freq]
            
            # Polish: Pythonic list checking
            if bucket:
                res.extend(bucket)
            
            # Polish: Break exactly when we hit capacity (or slightly exceed due to ties)
            if len(res) >= k:
                break
        
        # Brilliant guard against bucket ties
        return res[:k]