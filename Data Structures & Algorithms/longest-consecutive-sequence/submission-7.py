class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        for num in nums: 
            if not (num-1) in nums_set:
                curr_seq = 1
                next_num = num+1
                while next_num in nums_set:
                    curr_seq+=1
                    next_num+=1
                
                max_seq = max(curr_seq, max_seq)
        
        return max_seq