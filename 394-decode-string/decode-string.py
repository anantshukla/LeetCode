class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                outStr = ""
                while stack[-1] != '[':
                    outStr = stack.pop() + outStr
                stack.pop()
                
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                stack.append(outStr * int(multiplier))
        
        return "".join(stack)
