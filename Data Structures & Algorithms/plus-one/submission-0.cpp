class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> final_answer;
        int sum = 0;
        int iDigit = 0;

        for (auto& c : digits) {
            sum = sum*10 + c; 
        }   
        sum ++;
        while (sum>0) {
            final_answer.insert(final_answer.begin(),sum % 10);
            sum = sum / 10;
        }
        return final_answer;
    }
};
