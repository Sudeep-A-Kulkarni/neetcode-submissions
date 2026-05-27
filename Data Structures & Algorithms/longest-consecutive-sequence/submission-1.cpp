class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if (nums.empty()) {
            return 0;
        }
        
        int temp = 0;
        int max_length = 0;
        int count = 1;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
                if (nums[i] > nums[j]){
                    temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }   
            }
        }

        for ( int k = 0; k < nums.size() - 1; k++) {
            if (nums[k+1] == nums[k] + 1) {
                count ++;
            } else if (nums[k] == nums[k+1]) {
                continue;
            } else {
                if (max_length < count) {
                    max_length = count;
                }
                count = 1;
            }
        }

        if (max_length < count) {
            max_length = count;
        }

        return max_length;
    }
};
