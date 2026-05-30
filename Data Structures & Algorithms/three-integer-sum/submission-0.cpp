class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {

                    if (nums[i] + nums[j] + nums[k] == 0) {

                        vector<int> target =
                            {nums[i], nums[j], nums[k]};

                        if (find(ans.begin(),
                                 ans.end(),
                                 target) == ans.end()) {

                            ans.push_back(target);
                        }
                    }
                }
            }
        }

        return ans;
    }
};