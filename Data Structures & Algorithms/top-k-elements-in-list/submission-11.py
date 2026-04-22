from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq_map = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            freq_map[cnt].append(num)

        i = 0
        k_freq = []
        j = len(nums) -1
        while i < k:
            for num in freq_map[j]:
                k_freq.append(num)
                i+=1
                if i == k:
                    return k_freq
            j-=1

        return k_freq

