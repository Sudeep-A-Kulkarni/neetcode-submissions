class Solution {
    public boolean hasDuplicate(int[] nums) {

        int i = 0, j = 0;
        boolean bFlag = false;

        for ( i = 0; i < nums.length; i++) {
            for ( j = (i + 1); j < nums.length; j++)
            {
                if ( nums[i] == nums[j] ) {
                    bFlag = true;
                }
            }
        }
        
        return bFlag;
    }
}