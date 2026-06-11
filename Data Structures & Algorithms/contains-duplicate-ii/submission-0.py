class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}  # Maps: number -> its most recent index
        
        for i, num in enumerate(nums):
            # If we've seen this number before AND it's close enough, we're done!
            if num in last_seen and i - last_seen[num] <= k:
                return True
            
            # Update the map with the current index
            last_seen[num] = i
            
        return False