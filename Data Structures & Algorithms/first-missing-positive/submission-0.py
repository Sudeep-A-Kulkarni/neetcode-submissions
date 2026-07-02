class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # Keep swapping until the element at index i is in its correct slot,
            # or it is out of bounds (<= 0 or > n), or it's a duplicate.
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Swap nums[i] with the element at its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Second pass: find the first index where the value doesn't match the index rule
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all positions are correct, the missing number is n + 1
        return n + 1