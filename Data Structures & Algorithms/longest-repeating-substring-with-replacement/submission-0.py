
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # Add current character to frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # Check if current window requires more than k replacements
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Track the maximum valid window size
            max_length = max(max_length, right - left + 1)
            
        return max_length
