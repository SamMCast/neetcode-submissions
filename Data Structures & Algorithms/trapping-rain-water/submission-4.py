class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        left_wall = height[left]
        right_wall = height[right]
        water = 0

        while left < right:
            if left_wall < right_wall:
                left +=1
                ground = height[left]
                left_wall = max(left_wall, ground)
                water += left_wall - ground
            
            else:
                right -=1
                ground = height[right]
                right_wall = max(right_wall, ground)
                water += right_wall - ground
        
        return water