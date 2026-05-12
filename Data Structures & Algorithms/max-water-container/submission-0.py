class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) -1
        max_water_amount = current_water_amount = 0

        while left < right:
            current_water_amount = (right - left) * (min(heights[left], heights[right]))
            max_water_amount = max(current_water_amount, max_water_amount)
            if heights[left] < heights[right]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                right -=1
                left+=1
        
        return max_water_amount
