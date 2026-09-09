class Solution:
    def maxBuilding(self, n, restrictions):
        # Building 1 must have height 0
        restrictions.append([1, 0])

        # Add building n as a boundary.
        # If n already exists, don't add another restriction.
        if not any(x[0] == n for x in restrictions):
            restrictions.append([n, n - 1])

        # Sort by building number
        restrictions.sort()

        # Forward pass
        for i in range(1, len(restrictions)):
            prev_id = restrictions[i - 1][0]
            prev_height = restrictions[i - 1][1]

            curr_id = restrictions[i][0]
            curr_height = restrictions[i][1]

            restrictions[i][1] = min(
                curr_height,
                prev_height + (curr_id - prev_id)
            )

        # Backward pass
        for i in range(len(restrictions) - 2, -1, -1):
            curr_id = restrictions[i][0]
            curr_height = restrictions[i][1]

            next_id = restrictions[i + 1][0]
            next_height = restrictions[i + 1][1]

            restrictions[i][1] = min(
                curr_height,
                next_height + (next_id - curr_id)
            )

        ans = 0

        # Find maximum possible peak
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]

            distance = id2 - id1

            # Maximum peak between the two restrictions
            peak = (h1 + h2 + distance) // 2

            ans = max(ans, peak)

        return ans