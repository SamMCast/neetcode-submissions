class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            num_at_k = nums[k]
            left = k + 1
            right = len(nums)-1
            while left < right:
                num_at_i = nums[left]
                num_at_j = nums[right]
                current_sum = num_at_k + num_at_i + num_at_j 
                if current_sum < 0:
                    left+=1
                    continue
                elif current_sum > 0:
                    right-=1
                    continue
                
                res.append([num_at_k, num_at_i, num_at_j])
                left+=1
                right-=1
                while left < right and nums[left] == nums[left-1] and nums[right] == nums[right+1]:
                    left+=1
                    right-=1
                    
        
        return res
                

