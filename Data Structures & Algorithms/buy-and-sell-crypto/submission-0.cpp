class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0;
        int max_profit = 0, min = 0;
        int pos = 0;
        min = prices[0];
        for (i = 0; i < prices.size(); i++) {
            if (prices[i] < min) {
                min = prices[i];
            }
            int profit = prices[i] - min;

            if ( profit > max_profit ) {
                max_profit = profit;
            }
        }
        return max_profit;
    }
};
