class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Handles 0 and 1 immediately

        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            
            if num > x:
                right = pivot - 1  # Too big, search the lower half
            elif num < x:
                left = pivot + 1   # Too small, search the upper half
            else:
                return pivot       # Perfect square found
                
        return right  # 'right' will naturally land on the truncated integer floor
