class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                last = stack.pop()
                stack.append(math.trunc(stack.pop() / float(last)))
            else:
                stack.append(int(token))
        return stack[0]
