class Solution:
    def evaluate(self, s, knowledge):
        # Store knowledge in a dictionary
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):

            # If we find an opening bracket
            if s[i] == '(':

                # Find the closing bracket
                j = i + 1

                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Add value if key exists, otherwise '?'
                if key in mp:
                    result.append(mp[key])
                else:
                    result.append('?')

                # Move after ')'
                i = j + 1

            else:
                # Normal character
                result.append(s[i])
                i += 1

        return ''.join(result)