class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in s:
            if letter not in t:
                return False

        return True
            

        