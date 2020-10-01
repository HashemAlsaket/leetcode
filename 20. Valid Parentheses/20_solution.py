class Solution:
    def isValid(self, s: str) -> bool:
        
        l = "([{"
        stack = []
        
        s = [x for x in s] # convert to list for easier handling
        
        while s:
            paren = s.pop(0)
            if paren in l:
                stack.append(paren)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if p=='(':
                    if paren!=')':
                        return False
                if p=='[':
                    if paren!=']':
                        return False
                if p=='{':
                    if paren!='}':
                        return False
        if stack:
            return False
        return True
        
        
        