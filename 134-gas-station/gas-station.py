class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]

        # Not enough gas overall
        if total_gas < total_cost:
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # Current start cannot reach i
            if tank < 0:
                start = i + 1
                tank = 0

        return start