class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        I'm thinking a two pointer solution i and j. 
        i = 0 j= 0
        nums = [1,1,2,3,4]
        increment j until you reach pos 2 why because nums[2] != val
        set nums[i] = nums[j]
        nums = [2, 1, 2, 3, 4]
        increment i = 1
        increment j until 3 why because nums[j] (nums[3]) != val
        set nums[i] = nums[j]
        [2,3, 2, 3, 4]
        increment  i = 2 nums[i]
        nums = []
        Pointer i increments only when element at the current 
        position doesn't equal val. Pointer j is responsible for finding the next element
        that equals val. If the element at pointer i does equal val, increment pointer j 
        from pointer i until element that doesn't equal val is found. If pointer j is out of bounds 
        return pointer i +1 as k. 
        '''
        i = j = 0
        n = len(nums)
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                
                i+=1
        
        return i

