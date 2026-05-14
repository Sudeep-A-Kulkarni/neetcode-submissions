class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int i = 0, j = 0;
        bool bFlag = false;

        for ( i = 0; i < nums.size(); i++)
        {
            for ( j = i + 1; j < nums.size(); j++)
            {
                if (nums[i] == nums[j])
                {
                    bFlag = true;
                }
            }
        }
        return bFlag;        
    }
};