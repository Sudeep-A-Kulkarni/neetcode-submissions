class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0;

        for (int i = 0; i < matrix.size(); i ++) {
            if (!((matrix[i][matrix[0].size()-1]) < target)) {
                row = i;
                break;
            }
        }

        for (int j = 0; j < matrix[0].size(); j++) {
            if (matrix[row][j] == target) {
                return true;
            }
        }
       return false;
    }
};