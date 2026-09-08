class Solution:
    def processStr(self, s):
        result = []

        for ch in s:
            if ch.islower():
                # Append character
                result.append(ch)

            elif ch == '*':
                # Remove last character if it exists
                if result:
                    result.pop()

            elif ch == '#':
                # Duplicate the current result
                result += result.copy()

            elif ch == '%':
                # Reverse the result
                result.reverse()

        return ''.join(result)