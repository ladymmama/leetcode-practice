class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # TC:O(log n), SC: O(1)
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:  # if mid-right is ascending order, it the first part
                if target > nums[mid] and target <= nums[right]:  # if target in this parts
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if target < nums[mid] and target >= nums[left]:  # left part
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

    # 4,5,6,7,0,1,2,3 target 2
    # left = 0, right = 7, mid = 3
    # mid > right -> enter the else loop: 2 < num[left] -> enter the else, increase left 