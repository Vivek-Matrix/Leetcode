class Solution:
    def isValid(self, s: str) -> bool:
        stack, lefts, rights = [], ('(','[','{'), (')',']','}')
        for b in s:
            if b in lefts:
                stack.append(b)
            elif not stack or lefts.index(stack.pop())!=rights.index(b):
                return False
        return not stack