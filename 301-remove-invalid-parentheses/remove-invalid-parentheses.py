class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        # BFS
        queue = {s}
        visited = {s}

        while queue:
            valid = []

            # Check current level
            for string in queue:
                if is_valid(string):
                    valid.append(string)

            # If valid strings are found,
            # they required minimum removals
            if valid:
                return valid

            # Generate next level
            next_level = set()

            for string in queue:
                for i in range(len(string)):
                    # Only remove parentheses
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.add(new_string)

            queue = next_level

        return [""]