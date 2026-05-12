class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1

        left_boundary_height = height[left]
        right_boundary_height = height[right]
        water = 0
        while left < right:
            

            if left_boundary_height < right_boundary_height:
                ground = left+1
                left_boundary_height = max(left_boundary_height, height[ground])
                water += left_boundary_height - height[ground]
                left +=1
            else:
                ground = right -1
                right_boundary_height = max(right_boundary_height, height[ground] )
                water += right_boundary_height - height[ground]
                right -=1
        
        return water
