class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int row = -1;

        for (int i = 0; i < matrix.size(); i++) {
            if (matrix[i][0] <= target &&
                target <= matrix[i][matrix[0].size() - 1]) {
                row = i;
                break;
            }
        }

        if (row == -1)
            return false;

        for (int j = 0; j < matrix[0].size(); j++) {
            if (matrix[row][j] == target)
                return true;
        }

        return false;
    }
};