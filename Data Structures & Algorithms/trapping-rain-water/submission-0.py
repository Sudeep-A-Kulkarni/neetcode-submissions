class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0
        
        while left < right:
            # The smaller boundary dictates the water level
            if left_max < right_max:
                left += 1
                # Update the running maximum from the left
                left_max = max(left_max, height[left])
                # Water trapped is the boundary height minus the current bar height
                total_water += left_max - height[left]
            else:
                right -= 1
                # Update the running maximum from the right
                right_max = max(right_max, height[right])
                # Water trapped is the boundary height minus the current bar height
                total_water += right_max - height[right]
                
        return total_water