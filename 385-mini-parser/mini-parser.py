class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # Single integer
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        i = 0

        while i < len(s):
            if s[i] == '[':
                stack.append(NestedInteger())
                i += 1

            elif s[i] == ']':
                ni = stack.pop()

                if not stack:
                    return ni

                stack[-1].add(ni)
                i += 1

            elif s[i] == ',':
                i += 1

            else:
                j = i

                if s[j] == '-':
                    j += 1

                while j < len(s) and s[j].isdigit():
                    j += 1

                num = int(s[i:j])
                stack[-1].add(NestedInteger(num))

                i = j
        