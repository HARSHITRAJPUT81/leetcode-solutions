class Solution:
    def diffWaysToCompute(self, expression):
        memo = {}

        def solve(exp):
            if exp in memo:
                return memo[exp]

            res = []

            for i, ch in enumerate(exp):
                if ch in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])

                    for l in left:
                        for r in right:
                            if ch == "+":
                                res.append(l + r)
                            elif ch == "-":
                                res.append(l - r)
                            else:
                                res.append(l * r)

            # Base case: exp is a number
            if not res:
                res.append(int(exp))

            memo[exp] = res
            return res

        return solve(expression)