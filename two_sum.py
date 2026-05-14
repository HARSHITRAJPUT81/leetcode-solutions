5. Longest Palindromic Substring
Given a string s, return the longest Palindromic Substring in s.  


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
    
    

solution:- 

class Solution:

    def longestPalindrome(self, s):

        # Store the longest palindrome
        answer = ""

        # Go through every character
        for i in range(len(s)):

            # ---------- Check odd length palindrome ----------

            left = i
            right = i

            # Expand while characters are same
            while left >= 0 and right < len(s) and s[left] == s[right]:

                current = s[left:right + 1]

                # Update answer if current palindrome is bigger
                if len(current) > len(answer):
                    answer = current

                left = left - 1
                right = right + 1


            # ---------- Check even length palindrome ----------

            left = i
            right = i + 1

            # Expand while characters are same
            while left >= 0 and right < len(s) and s[left] == s[right]:

                current = s[left:right + 1]

                # Update answer if current palindrome is bigger
                if len(current) > len(answer):
                    answer = current

                left = left - 1
                right = right + 1

        return answer

