class Solution:
    def trap(self, height: list[int]) -> int:
        slow = fast = water_sum = 0

        while fast < len(height):
            if slow + 1 >= len(height):
                return water_sum
                
            if height[slow + 1] >= height[slow]:
                slow += 1
                fast = slow
            else:
                fast = slow + 1
                while fast < len(height) and height[fast] < height[slow]:
                    fast += 1
                    
                # --- THE FIX STARTS HERE ---
                # If we couldn't find a wall taller than 'slow', fast falls off the edge.
                if fast == len(height):
                    # 1. Find the index of the tallest wall we have left
                    tallest_remaining_idx = slow + 1
                    for i in range(slow + 1, len(height)):
                        if height[i] > height[tallest_remaining_idx]:
                            tallest_remaining_idx = i
                    
                    # 2. Tell 'fast' to point at that sub-optimal wall
                    fast = tallest_remaining_idx
                    
                    # 3. Our water is now restricted by this shorter right wall
                    boundary_height = height[fast]
                else:
                    # Original logic: We found a taller wall, so 'slow' is our restriction
                    boundary_height = height[slow]
                # --- THE FIX ENDS HERE ---

                # Now do your exact calculation, but using boundary_height!
                while slow < fast - 1: # Added '-1' to stop BEFORE landing on the right wall
                    slow += 1
                    water_sum += boundary_height - height[slow]
                
                # Snap slow to the new wall to start the next hunt!
                slow = fast
                
        return water_sum