class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> umap;

        for (auto& c : strs) {
            string temp = c;
            sort(c.begin(), c.end());
            umap[c].push_back(temp);
        }

        for ( auto& c : umap ) {
            ans.push_back(c.second);
        }
       
       return ans;
    }
};
