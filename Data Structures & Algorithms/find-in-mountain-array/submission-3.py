# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # Step 1: Find the peak element
        low, high = 0, n - 1
        peak = 0
        while low <= high:
            mid = (low + high) // 2
            # Handle boundary cases safely; constraints guarantee peak is not at index 0 or n-1
            if mid == 0:
                low = mid + 1
            elif mid == n - 1:
                high = mid - 1
            else:
                mid_val = mountain_arr.get(mid)
                right_val = mountain_arr.get(mid + 1)
                
                if mid_val < right_val:
                    # We are on the rising slope, peak is to the right
                    low = mid + 1
                else:
                    # We are on the falling slope, mid could be the peak or peak is to the left
                    peak = mid
                    high = mid - 1
                    
        # Step 2: Binary search on the strictly increasing left side
        low, high = 0, peak
        while low <= high:
            mid = (low + high) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        # Step 3: Binary search on the strictly decreasing right side
        low, high = peak, n - 1
        while low <= high:
            mid = (low + high) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:  # Note the flipped condition for the descending slope
                low = mid + 1
            else:
                high = mid - 1
                
        return -1