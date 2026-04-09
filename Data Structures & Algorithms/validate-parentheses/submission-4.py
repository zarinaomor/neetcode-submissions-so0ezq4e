class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', ']' : '[', '}' : '{' }

        for c in s:
            # this line checks if it is the closing parenthesis.
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            
            # if it is the Open parenthesis then add it to stack
            else:
                stack.append(c)

        return True if not stack else False






















        stack = []
        hashMap = {'}':'{', ')':'(', ']':'['}

        for c in s:
            if c in hashMap:
                if stack and stack[-1] == hashMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
        