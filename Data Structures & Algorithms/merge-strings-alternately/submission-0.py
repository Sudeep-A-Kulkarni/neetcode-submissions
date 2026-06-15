class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        op_string = ""
        # Loop up to the length of the longer word
        for i in range(max(len(word1), len(word2))):
            # i:i+1 safely returns empty string if index is out of bounds
            op_string += word1[i:i+1] + word2[i:i+1]
            
        return op_string

        
        