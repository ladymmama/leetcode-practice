class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        i = 0

        while i <= two:
            if nums[i] == 0:  # if we find nums[i] == 0
                nums[zero], nums[i] = nums[i], nums[zero]  # swap this their position
                i += 1  # keep move i to the right
                zero += 1  # and also we move zero to next position
            elif nums[i] == 1:  # if nums[i] == 1, we just keep move the i to the right
                i += 1
            elif nums[i] == 2:  # if we finf nums[i] == 2
                nums[two], nums[i] = nums[i], nums[two]  # we swap the position of this number with the end position.
                two -= 1  # and we move the two to one left position

        """
        # we can also use counter to solve this one since there are only 3 numbers.
        count = collections.Counter(nums)
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2

        """
