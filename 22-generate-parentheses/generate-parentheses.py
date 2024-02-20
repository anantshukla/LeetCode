class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk, ans = [], []
        def permute(openCount, closedCount):
            if openCount == closedCount == n:
                ans.append("".join(stk))
                return
            if openCount < n:
                stk.append('(')
                permute(openCount + 1, closedCount)
                stk.pop()
            if closedCount < openCount:
                stk.append(')')
                permute(openCount, closedCount + 1)
                stk.pop()
        permute(0, 0)
        return ans
        