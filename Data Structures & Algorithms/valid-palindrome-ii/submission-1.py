class Solution:
    def validPalindrome(self, s: str) -> bool:
        reversed_String = s[::-1]
        count = 0

        if (reversed_String == s):
            return True
        
        left = 0
        right = len(s)-1

        while (left <= right):
            if (s[left] == s[right]):
                bFlag = True
            else:
                count += 1
        
            left+=1
            right-=1

        if (count == 1):
            return True
        else:
            return False


        