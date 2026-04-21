
'''
I need to identify the start of a sequence. I can do these three passes
the first pass would be to create a set since the elements in the sequence need
to be unique. The second pass would to identify the starting sequences 
and the last pass would to solve the problem
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
            
        numset = set()
        startlist = []
        longestseq = 1
        for val in nums:
            numset.add(val)
        
        for val in nums:
            prev = val -1
            succ = val + 1
            if prev in numset: # if there is an element before the current number move on
                continue
            if succ in numset: #if there is an element that is after it and not before it then this is the start of the sequence
                startlist.append(val)
                
        for num in startlist:
            nextnum = num
            currentseq = 1
            valid = True
            while valid:
                nextnum = nextnum + 1
                if nextnum in numset:
                    currentseq+=1
                else:
                    valid = False
            longestseq = max(longestseq, currentseq)
        return longestseq


            
        
        