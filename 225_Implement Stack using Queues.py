class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue = []

    def push(self, x: int):
        """
        Push element x onto stack.
        """
        temp = [x]
        self.queue = temp + self.queue

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.queue[0]
        self.queue[:] = self.queue[1:]
        return x

    def top(self):
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()