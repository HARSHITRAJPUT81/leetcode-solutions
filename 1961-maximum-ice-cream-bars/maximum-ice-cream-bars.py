class Solution:
    def maxIceCream(self, costs, coins):
        max_cost = max(costs)

        # Count frequency of each cost
        freq = [0] * (max_cost + 1)

        for cost in costs:
            freq[cost] += 1

        count = 0

        # Process costs from cheapest to most expensive
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue

            # Maximum number of bars we can afford at this price
            can_buy = min(freq[cost], coins // cost)

            count += can_buy
            coins -= can_buy * cost

            # No money left
            if coins == 0:
                break

        return count