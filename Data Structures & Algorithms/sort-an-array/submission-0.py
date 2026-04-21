import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        I could use heapqs as a sort method just to gain experience using heapqs
        I heapfy the array which is linear time. Then I constantly heappop (logN)
        into a a new array (N). The total operation is O(NlogN)
        '''
        res = [0 for x in nums]
        heapq.heapify(nums)
        for i,n in enumerate(res):
            res[i] = heapq.heappop(nums)
        
        return res
