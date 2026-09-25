class Solution:
    def braceExpansionII(self, expression):
        def parse(s, i):
            result = set()
            current = {""}

            while i < len(s) and s[i] != '}':
                
                if s[i] == '{':
                    # Parse expression inside braces
                    inside, i = parse(s, i + 1)

                    # Concatenate with current result
                    new_set = set()
                    for a in current:
                        for b in inside:
                            new_set.add(a + b)

                    current = new_set

                elif s[i].isalpha():
                    # Read a letter
                    new_set = set()

                    for word in current:
                        new_set.add(word + s[i])

                    current = new_set
                    i += 1

                elif s[i] == ',':
                    # Union current part into result
                    result.update(current)
                    current = {""}
                    i += 1

            # Add the last part
            result.update(current)

            return result, i + 1

        result, _ = parse(expression, 0)

        return sorted(result)