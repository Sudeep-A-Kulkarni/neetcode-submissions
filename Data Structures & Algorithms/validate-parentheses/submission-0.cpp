class Solution {
public:
    bool isValid(string s) {

        if (s.length() % 2 != 0) {
            return false;
        }

        char arr[s.length()];
        int top = -1;

        for (int i = 0; i < s.length(); i++) {

            // opening brackets
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                top++;
                arr[top] = s[i];
            }

            // closing brackets
            else {

                if (top == -1) {
                    return false;
                }

                if (s[i] == ')' && arr[top] != '(') {
                    return false;
                }

                if (s[i] == '}' && arr[top] != '{') {
                    return false;
                }

                if (s[i] == ']' && arr[top] != '[') {
                    return false;
                }

                top--;
            }
        }

        return (top == -1);
    }
};