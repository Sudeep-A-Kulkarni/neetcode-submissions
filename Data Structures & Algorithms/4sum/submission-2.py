class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans_list = []
        n = len(nums)
        
        # 1. Sort the entire list once at the beginning
        nums.sort()
        
        for i in range(n):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 2. Use two pointers for the remaining two numbers
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        ans_list.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        # Move both pointers inward
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1  # Sum is too small, move left pointer right
                    else:
                        right -= 1 # Sum is too big, move right pointer left
                        
        return ans_list
