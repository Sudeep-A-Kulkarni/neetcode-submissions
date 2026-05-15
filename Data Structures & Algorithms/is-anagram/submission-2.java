class Solution {
    public boolean isAnagram(String s, String t) {
        int[] Counter = new int[26];
        boolean bFlag = true;
        int i = 0;

        if (s.length() != t.length()) {
            return false;
        }

        for ( i = 0; i < s.length(); i++ ) {
            Counter[s.charAt(i) - 'a']++;
            Counter[t.charAt(i) - 'a']--;
        }

        for ( i = 0; i < 26; i++) {
            if (Counter[i] != 0)
            {
                bFlag = false;
            }
        }
        return bFlag;
    }
}
