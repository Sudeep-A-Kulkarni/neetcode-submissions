class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ((len(s)) != len(t)):
            return False
        for letter in s:
            if letter not in t:
                return False

        return True
            

        