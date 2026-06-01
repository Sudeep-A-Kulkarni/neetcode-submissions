class Solution {
public:
    int maxArea(vector<int>& heights) {
        int i = 0, j = 0;
        int dist = 0;
        int capacity = 0;
        int max_capacity = 0;

        for (i = 0; i < heights.size(); i++) {
            for (j = i+1; j < heights.size(); j++) {
                dist = j - i;
                capacity = dist * min(heights[i], heights[j]);
                if (max_capacity < capacity) {
                    max_capacity = capacity;
                }
            }
        }    
        return max_capacity;    
    }
};
