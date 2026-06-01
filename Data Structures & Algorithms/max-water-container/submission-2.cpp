class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0, right = 0;
        int max_water = 0;
        int capacity = 0;

        right = heights.size() - 1;

        while (left <= right) {
            capacity = (right-left) * min(heights[left], heights[right]);
            if (max_water < capacity) {
                max_water = capacity;
            }

            if (heights[left] > heights[right]) {
                right--;
            } else {
                left++;
            }
        }

        return max_water;
    }
};
