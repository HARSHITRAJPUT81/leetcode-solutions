from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(string):
            balance = 0
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        res = []
        visited = set([s])
        q = deque([s])
        found = False

        while q:
            cur = q.popleft()

            if isValid(cur):
                res.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in "()":
                    continue

                nxt = cur[:i] + cur[i + 1:]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return res