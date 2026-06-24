class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k > array length
        
        # Helper function to reverse a portion of the array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # 1. Reverse the entire array
        reverse(0, n - 1)
        # 2. Reverse the first k elements
        reverse(0, k - 1)
        # 3. Reverse the remaining elements
        reverse(k, n - 1)