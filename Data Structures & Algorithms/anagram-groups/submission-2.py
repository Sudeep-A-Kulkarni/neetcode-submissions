from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map a sorted word template to all of its original anagram variations
        anagram_groups = defaultdict(list)
        
        for word in strs:
            # "tea" sorted becomes "aet"
            sorted_word = "".join(sorted(word))
            # Group it safely
            anagram_groups[sorted_word].append(word)
            
        return list(anagram_groups.values())
 