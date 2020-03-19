class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TC: O(n), SC: O(n)
        d = collections.defaultdict(int)
        count = 0
        _sum = 0
        d[0] = 1
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum - k in d:
                count += d[
                    _sum - k]  # [a1, a2, a3], a1 = 3 , a3 =5 a3-a1 = k -> from a1 to a3, ther must be a subarray sum = k
            d[_sum] += 1
        return count

