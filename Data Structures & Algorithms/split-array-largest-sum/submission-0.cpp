class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        return dfs(nums, 0, k, n);
    }

private:
    int dfs(vector<int>& nums, int i, int m, int n) {
        if (i == n) {
            return m == 0 ? 0 : INT_MAX;
        }
        if (m == 0) {
            return INT_MAX;
        }

        int res = INT_MAX, curSum = 0;
        for (int j = i; j <= n - m; j++) {
            curSum += nums[j];
            res = min(res, max(curSum, dfs(nums, j + 1, m - 1, n)));
        }

        return res;
    }
};