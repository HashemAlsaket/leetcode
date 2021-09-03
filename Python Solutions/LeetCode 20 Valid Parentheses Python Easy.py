# Link to video: https://www.youtube.com/watch?v=1op9NieLYW4

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for l in s:
            if l in '({[':
                stack.append(l)
                continue
            if not stack:
                return False
            left = stack.pop()
            if l == ')' and left != '(':
                return False
            if l == '}' and left != '{':
                return False
            if l == ']' and left != '[':
                return False
        return len(stack) == 0