class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(0, len(nums)-1):
            if (nums[i] < target and nums[i+1] > target):
                nums.insert(i+1, target)
                return i+1
            elif(target > nums[len(nums)-1]):
                nums.insert(len(nums), target)
                return len(nums)-1
            elif(target < nums[0]):
                nums.insert(0, target)
                return 0
        
        

        


        