class Solution:
    def canJump(self, nums: List[int]) -> bool:
        des = len(nums) - 1  # define the destination
        for i in range(len(nums) - 1, -1, -1):  # from right to left to find the good position
            if i + nums[i] >= des:  # if i can get to the destination in num[i]
                des = i  # we make this i the next destination
        return des == 0  # if destination becomes 0, it can jump to the end
    # TC: O(n)  SC:O(1)
