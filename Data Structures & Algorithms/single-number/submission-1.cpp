class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> mymapp;
        int ans = 0;

        // Corrected the increment bug here
        for (int i = 0; i < nums.size(); i++) {
            mymapp[nums[i]]++; 
        }

        for (const auto& [key, value] : mymapp) {
            if (value == 1) {
                ans = key;
                break; // Optional: exit early once found
            }
        }
        return ans;
    }
};
