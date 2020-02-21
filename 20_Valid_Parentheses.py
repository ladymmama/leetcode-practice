class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # create a stack
        dic = {")": "(", "]": "[", "}": "{"}  # use dic to map the right pareneses
        for pa in s:
            if pa == '(' or pa == '[' or pa == '{':
                stack.append(pa)

                # corner case or if top of the stack is not matach to the dic like: (]
            elif pa == ')' or pa == ']' or pa == '}':
                if len(stack) == 0 or stack.pop() != dic[pa]:
                    return False

        return len(stack) == 0  # finally return if the stack is empty, then its true otherwise, its false. :)