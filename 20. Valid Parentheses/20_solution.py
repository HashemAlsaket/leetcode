# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        l = "([{"                     # Reference all left parentheses, brackets, 
                                      #     and braces
        stack = []                    # Set up a stack
        
        s = [x for x in s]            # Convert to list for easier handling
        
        while s:
            paren = s.pop(0)          # Get first character in string (now list)
            if paren in l:            # If character is one of left braces,
                stack.append(paren)   #     add it to the stack
            else:
                if not stack:         # If stack is empty there is no possible match
                    return False      #     for a left and right parentheses, etc.

                p = stack.pop()       # Since paren is not one of "([{", it must be
                                      #     one of "}])", so pop off the end of the 
                                      #     stack

                if p=='(':            # Check if there is a right match for any of
                    if paren!=')':    #     the left side characters in "([{"
                        return False
                if p=='[':
                    if paren!=']':
                        return False
                if p=='{':
                    if paren!='}':
                        return False
                                      
        if stack:                     # If there are still characters in the stack,
            return False              #     there is no possible match for the 
                                      #     remaining characters since s is now empty

        return True                   # If stack if empty, return True
        