class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Count frequencies
        unordered_map<int,int> freq;
        for (int x : nums) freq[x]++;
        
        // Move to vector of pairs (num, count)
        vector<pair<int,int>> v(freq.begin(), freq.end());
        
        // Sort by frequency descending
        sort(v.begin(), v.end(), [](const pair<int,int>& a, const pair<int,int>& b){
            if (a.second != b.second) return a.second > b.second;
            return a.first < b.first; // tie-breaker (optional)
        });
        
        // Take top k numbers
        vector<int> ans;
        for (int i = 0; i < k; ++i) ans.push_back(v[i].first);
        return ans;
    }
};