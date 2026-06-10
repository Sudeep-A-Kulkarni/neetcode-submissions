
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Loop from the second-to-last element down to 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == nums[i+1]:
                del nums[i]
        
        return len(nums)
