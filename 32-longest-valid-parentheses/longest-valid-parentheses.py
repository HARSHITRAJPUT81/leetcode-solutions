class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        ans = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    # Current ')' cannot be matched
                    stack.append(i)
                else:
                    # Length of valid substring
                    ans = max(ans, i - stack[-1])

        return ans