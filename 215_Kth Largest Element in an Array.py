class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        # TC: O(n+n/2+n/4..=2n) = O(n), SC: O(1)
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivotindex = self._partition(nums, left, right)
            if pivotindex == len(nums) - k:
                return nums[pivotindex]
            elif pivotindex > len(nums) - k:
                right = pivotindex - 1
            else:
                left = pivotindex + 1
        return -1

    def _partition(self, nums, left, right):
        index = left
        pivot = nums[right]

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1

        nums[right], nums[index] =  nums[index], nums[right]
        return index
        """
        # TC: O(n) + O(klogn) SC: O(1)
        heap = []
        heapq.heapify(heap)
        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])
        while k > 0:
            res = -heapq.heappop(heap)
            k -= 1
        return res
