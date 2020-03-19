class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        curr = 0
        res = ""
        for i in range(max(len(a), len(b))):
            curr = carry
            if i < len(a):
                curr += int(a[-1 - i])
            if i < len(b):
                curr += int(b[-1 - i])
            carry = curr // 2
            res += str(curr % 2)

        if carry:
            res += str(carry)

        return res[::-1]
