class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPos = [[pos, speed] for pos, speed in zip(position, speed)]
        stack = []

        for p, s in sorted(carPos)[::-1]:
            stack.append((target - p)/s)
            if len(stack) > 1:
                print(stack[-1], stack[-2])
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
