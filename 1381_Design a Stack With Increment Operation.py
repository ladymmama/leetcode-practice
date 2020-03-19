class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.max_Size = maxSize
        self.stack = [] * maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.max_Size:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if not self.stack:
            pass
        elif len(self.stack) <= k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for j in range(0, k):
                self.stack[j] = self.stack[j] + val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)