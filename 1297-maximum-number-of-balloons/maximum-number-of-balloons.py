class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"

        wordCount, textCount = defaultdict(int), defaultdict(int)
        for c in word:
            wordCount[c] += 1
        for c in text:
            textCount[c] += 1

        return min(
            [textCount[char] // wordCount[char] for char in wordCount]
        )
        