class Solution:
    def decodeString(self, s: str) -> str:
        stack, ptr = [], 0
        while ptr < len(s):
            if s[ptr] != ']':
                stack.append(s[ptr])
            else:
                outStr = ""
                while stack[-1] != '[':
                    outStr = stack.pop() + outStr
                stack.pop()
                
                multiplicationFactor = ""
                while stack and stack[-1].isdigit():
                    multiplicationFactor = stack.pop() + multiplicationFactor
                multiplicationFactor = int(multiplicationFactor)
                outStr = outStr * multiplicationFactor
                stack.append(outStr)
            ptr += 1
        outStr = ""
        while stack:
            outStr = stack.pop() + outStr
        return outStr
