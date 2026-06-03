class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> character_map;

        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {

            character_map[s[right]]++;

            while (character_map[s[right]] > 1) {
                character_map[s[left]]--;
                left++;
            }

            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};

