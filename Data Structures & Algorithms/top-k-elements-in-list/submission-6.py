'''
Sol 1: Min heap of pair(element frequency, element)
time complexity: We build of a min heap of size k where each element is a pair consisting of the frequency
count and the value. Consistently popping the min element(least frequent) means that we will be left the k
most frequent elements. Over an array of size n we will be popping and adding are O(logk), so the final operation 
will be O(nlogk)
space complexity: The number of distinct elements will always be bounded by the array size which is n. 
the heap size will be of size k so space will be O(n+k)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        
        res = []
        for key, v in count.items():
            heapq.heappush(res, (v, key))
            if len(res) > k:
                heapq.heappop(res)
        
        return [x[1] for x in res]