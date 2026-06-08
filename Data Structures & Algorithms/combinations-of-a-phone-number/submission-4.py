import itertools

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Handle the empty input test case
        if not digits:
            return []
        
        # Standard native mapping (RangeKeyDict is not supported on NeetCode)
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # 1. Fetch the mapped letter arrays for each digit provided
        letter_lists = [phone_map[d] for d in digits]
        
        # 2. Use the * unpacking operator to generate cross-product pairings
        combinations = itertools.product(*letter_lists)
        
        # 3. Clean up the output: Join tuple components back into single strings
        return ["".join(item) for item in combinations]
