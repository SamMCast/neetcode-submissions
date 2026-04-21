class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums_set = set(nums)
        num = nums_set.pop()
        max_seq = curr_seq = 1
      
        while nums_set:
            prev = num -1
            succ = num + 1
            while prev in nums_set:
                curr_seq+=1
                nums_set.remove(prev)
                prev = prev -1
            while succ in nums_set:
                curr_seq +=1
                nums_set.remove(succ)
                succ = succ +1
            max_seq = max(curr_seq, max_seq)

            if len(nums_set) > 0:
                num = nums_set.pop()
                curr_seq = 1
        

        return max_seq

            
