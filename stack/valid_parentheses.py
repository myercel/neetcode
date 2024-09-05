"""
Problem No. 20

Given a string s containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "([])"
    Output: true

Example 2:
    Input: s = "(]"
    Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        stack.append(s[0])
        i = 1

        while i < len(s):
            # opening bracket
            if s[i] in brackets.values():
                stack.append(s[i])
            else: # closing bracket
                if stack and stack[-1] == brackets[s[i]]:
                    stack.pop()
                else:
                    return False
            i += 1

        return True if not stack else False