'''
Sol 1: Min heap of pair(element frequency, element)
time complexity: We build of a min heap of size k where each element is a pair consisting of the frequency
count and the value. Consistently popping the min element(least frequent) means that we will be left the k
most frequent elements. Over an array of size n we will be popping and adding are O(logk), so the final operation 
will be O(nlogk)
space complexity: The number of distinct elements will always be bounded by the array size which is n. 
the heap size will be of size k so space will be O(n+k)
Sol 2: Bucket list
time complexity: We generate a frequency table that is the size of the array since the max frequency is bounded
by the size of the array. We iterate through the array in reverse up to k. Time complexity O(n)
Space complexity: We generate a frequency table that is the size of the array. Max frequency can only ever be
the array size. O(n)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for x in range(0, len(nums)+1)]
        count = defaultdict(int)
        res = []
        for n in nums:
            count[n]+=1
        
        for key, v in count.items():
            freq[v].append(key)
        
        c = 0
        for i in range(len(nums),0, -1):
            if len(freq[i]) > 0:
                for e in freq[i]:
                    res.append(e)
                    k-=1
                    if k == 0:
                        return res
        return res


        