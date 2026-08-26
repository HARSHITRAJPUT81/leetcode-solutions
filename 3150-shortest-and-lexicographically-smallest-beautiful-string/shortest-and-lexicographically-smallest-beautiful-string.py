class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        answer = ""

        for right in range(len(s)):

            # Include current character
            if s[right] == '1':
                ones += 1

            # If more than k ones, shrink the window
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Remove unnecessary leading zeros
            while ones == k and s[left] == '0':
                left += 1

            # If window contains exactly k ones
            if ones == k:
                current = s[left:right + 1]

                # Choose shorter substring,
                # or lexicographically smaller if lengths are equal
                if (answer == "" or
                    len(current) < len(answer) or
                    (len(current) == len(answer) and current < answer)):
                    
                    answer = current

        return answer