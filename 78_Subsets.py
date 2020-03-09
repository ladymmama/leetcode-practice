class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        # the first solution is use recursion
        # TC: O(N*2^N) SC:O(N*2^N)
        # [[]]-> [[], [1]] -> + [[2], [1,2]] every time we loop we add the lastest
        res = [[]]
        for num in nums:
            res += [[num] + curr for curr in res]
        return res


        # This one is using backtracking
        # TC: O(N*2^N) SC:O(N*2^N)
        res = []
        # if needed, we can sort nums by nums.sort()
        if not nums:
            return [[]]
        if len(nums) == 1:          #if there is only one element, so subset is empty set and it self.
            return([ [],[nums[0]] ]) # check the first two if, we can know when to end the recursion

        prev = self.subsets(nums[:-1])  #define the prev answer
        curr = []
        for item in prev:               #all sets' sub set = prev set + every item in the prev set + the new element
            curr.append(item + [nums[-1]])
        res = prev + curr
        return res
        """
        # this is also backtraicking
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])