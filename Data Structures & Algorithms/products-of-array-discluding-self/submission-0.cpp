class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector <int> output;
        int product = 1;
        int i = 0, j = 0;

        for (j = 0; j < nums.size(); j++) {
            product = 1;
            for ( i = 0; i < nums.size(); i++ ) {
                if (i != j) {
                    product = product * nums[i];
                }
            }
            output.insert(output.begin()+j, product);
        }
        

        return output;
    }
};
