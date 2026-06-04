class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = {}
        
        # Step 1: Build the frequency map
        for no in nums:
            mydict[no] = mydict.get(no, 0) + 1
  
        # Step 2: Directly find and return the key with the max value
        return max(mydict, key=mydict.get)