class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        while len(nums_set) > max_seq :
            num = nums_set.pop()
            prev_num = num-1
            next_num = num + 1
            curr_seq = 1
            while prev_num in nums_set:
                curr_seq+=1
                nums_set.remove(prev_num)
                prev_num -=1
            while next_num in nums_set:
                curr_seq +=1 
                nums_set.remove(next_num)
                next_num +=1
            
            max_seq = max(max_seq, curr_seq)

        return max_seq