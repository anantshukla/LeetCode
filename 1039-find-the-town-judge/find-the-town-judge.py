class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        deltaEdges = defaultdict(int) # incoming - outgoing

        for out, inc in trust:
            deltaEdges[inc] += 1
            deltaEdges[out] -= 1
        
        for i in range(1, n + 1):
            if deltaEdges[i] == (n - 1):
                return i
        return -1
        
        # incoming = defaultdict(int)
        # outgoing = defaultdict(int)

        # for out, inc in trust:
        #     outgoing[out] += 1
        #     incoming[inc] += 1
        
        # for i in range(1, n + 1):
        #     if outgoing[i] == 0 and incoming[i] == (n - 1):
        #         return i
        # return -1
        