class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            if c == ')' and (len(stack)==0 or stack.pop()!=c):
                return False
            if c == '[':
                stack.append(']')
            if c == ']' and (len(stack)==0 or stack.pop()!=c):
                return False
            if c == '{':
                stack.append('}')
            if c == '}' and (len(stack)==0 or stack.pop()!=c):
                return False
        
        return len(stack)==0