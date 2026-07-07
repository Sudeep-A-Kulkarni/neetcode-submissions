class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # Search space is for the starting index of the window
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            # Compare distance of x from arr[mid] vs arr[mid + k]
            # If x is closer to arr[mid + k], move the window right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        # Return the window of length k starting at index 'left'
        return arr[left:left + k]
