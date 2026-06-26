class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        // Sort to easily access the heaviest and lightest remaining people
        sort(people.begin(), people.end());
        
        int boats = 0;
        int l = 0;                  // Lightest pointer
        int r = people.size() - 1;  // Heaviest pointer
        
        while (l <= r) {
            // If the heaviest and lightest can share, move the left pointer
            if (people[l] + people[r] <= limit) {
                l++;
            }
            // The heaviest person always takes up a boat slot
            r--;
            boats++;
        }
        
        return boats;
    }
};