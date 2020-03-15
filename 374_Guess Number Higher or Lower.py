# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            ret = guess(mid)

            if ret == 0:
                return mid
            elif ret == -1:
                right = mid - 1
            else:
                left = mid + 1