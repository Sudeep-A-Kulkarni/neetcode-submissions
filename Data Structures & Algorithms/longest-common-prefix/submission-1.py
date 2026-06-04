
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Take the first word as the reference baseline
        first_word = strs[0]
        
        for i in range(len(first_word)):
            char = first_word[i]
            # Check this character position against all other words
            for other_word in strs[1:]:
                # Stop if the current word is too short OR characters mismatch
                if i == len(other_word) or other_word[i] != char:
                    return first_word[:i]
                    
        return first_word
