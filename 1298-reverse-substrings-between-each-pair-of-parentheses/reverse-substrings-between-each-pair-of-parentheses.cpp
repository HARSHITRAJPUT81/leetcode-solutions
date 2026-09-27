#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string reverseParentheses(string s) {

        stack<string> st;
        string curr = "";

        for (char c : s) {

            if (c == '(') {
                // Save the string before '('
                st.push(curr);
                curr = "";
            }
            else if (c == ')') {

                // Reverse the innermost substring
                reverse(curr.begin(), curr.end());

                // Add it to the previous string
                curr = st.top() + curr;
                st.pop();
            }
            else {
                // Normal character
                curr += c;
            }
        }

        return curr;
    }
};