class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # This pointer tracks where the next valid element should go
        index = 0
        
        for no in nums:
            # If the current number is NOT the one we want to remove
            if no != val:
                # Move it to our tracked position
                nums[index] = no
                index += 1
                
        # 'index' now naturally equals the count of valid elements
        return index


            
        