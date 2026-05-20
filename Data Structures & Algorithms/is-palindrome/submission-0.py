class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Clean the string: keep only alphanumeric characters and lowercase them
        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        # 2. Compare the cleaned string with its reverse
        return cleaned_str == cleaned_str[::-1]
