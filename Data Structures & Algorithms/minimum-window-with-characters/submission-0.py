from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
            
        # Count frequency of characters in t
        t_count = Counter(t)
        window_count = {}
        
        # Track number of unique characters that match target frequency
        have, required = 0, len(t_count)
        
        # Track best window bounds [length, left_index, right_index]
        res = [float('inf'), 0, 0]
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If frequency matches requirement, increment 'have'
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
                
            # Contract the window from the left while it remains valid
            while have == required:
                # Update result if this window is smaller
                window_len = right - left + 1
                if window_len < res[0]:
                    res = [window_len, left, right]
                    
                # Pop out left character and shift left pointer
                left_char = s[left]
                window_count[left_char] -= 1
                
                # If removing left_char breaks the valid condition, decrement 'have'
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                    
                left += 1
                
        # Return the substring if a valid window was found
        return s[res[1]:res[2] + 1] if res[0] != float('inf') else ""
