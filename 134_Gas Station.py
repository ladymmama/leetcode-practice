class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        # gas[i] - cost[i] > 0
        # gas[i] - cost[i] + gas[i+1] - cost[i+1] > 0
        curr = 0
        for i in range(len(gas)):
            j = i
            curr = gas[j]
            while curr >= cost[j]:
                curr -= cost[j]
                j += 1
                j %= len(gas)
                if i == j:
                    print(1)
                    return i
                curr += gas[j]
        return -1
        """
        sum_gas = 0
        total = 0
        j = 0
        for i in range(len(gas)):
            sum_gas += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if sum_gas < 0:
                j = i + 1
                sum_gas = 0
        if total < 0:
            return -1
        else:
            return j