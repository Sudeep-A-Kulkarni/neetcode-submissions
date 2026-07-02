class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        # Step 1: Initialize two candidates and their counters
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        # First pass to find the potential candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                # If it's a completely different third element, 
                # discard one vote from both candidates
                count1 -= 1
                count2 -= 1
                
        # Step 2: Second pass to verify if candidates cross the n/3 threshold
        result = []
        n = len(nums)
        
        # Reset counts for verification
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
                
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
            
        return result