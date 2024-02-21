class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = [] # ind, val
        for idx, curr_temp in enumerate(temperatures):
            while len(stk) > 0 and curr_temp > stk[-1][1]:
                stk_idx, stk_temp = stk.pop()
                ans[stk_idx] = idx - stk_idx
            stk.append([idx, curr_temp])
        return ans            

            
        return ans

    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     n = len(temperatures)
    #     ans = [0] * n
    #     for i in range(0, n):
    #         for j in range(i + 1, n):
    #             if temperatures[i] < temperatures[j]:
    #                 ans[i] = j - i
    #                 break
    #     return ans

            
        