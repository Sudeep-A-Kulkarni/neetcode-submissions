class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0, j = 0;
        vector<int> answer;
        bool bFlag = false;
        for (i = 0; i < numbers.size() && !bFlag; i++) {
            for (j = i+1; j < numbers.size(); j++) {
                if (numbers[i] + numbers[j] == target) {
                    return {i+1, j+1};
                }
            }
        }
        return {};
    }
};
