class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Map to store (prefix_sum -> frequency)
        prefix_sums = {0: 1}
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - k) exists in past prefix sums, 
            # it means a subarray summing to k exists.
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
                
            # Record the current prefix sum in the map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count
        