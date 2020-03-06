class Solution:
    def jump(self, nums: List[int]) -> int:
        last, curr = 0, 0
        res = 0
        for i in range(len(nums)):
            if i > last:  # if the current position is greater than most far position, step += 1
                res += 1
                last = curr  # then give the new far position.

            curr = max(curr, i + nums[i])
        return res
    # TC: O(n), SC: O(1)

    # i = 0, last = 0, curr = 2   res = 0
    # i = 1, last = 2, curr = 4   res = 1 i > last
    # i = 2, last = 2, curr = 4   res = 1
    # i = 3, last = 4, curr = 4   res = 2 i > last
    # i = 4, last = 4, curr = 8   res = 2