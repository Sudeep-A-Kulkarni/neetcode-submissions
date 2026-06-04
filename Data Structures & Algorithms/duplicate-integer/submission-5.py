class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for number in nums:
            # Check if the number is already in the set
            if number in seen:
                return True
            seen.add(number)
        return False
