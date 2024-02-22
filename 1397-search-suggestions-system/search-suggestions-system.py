class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, r = 0, len(products) - 1
        result = []

        for i in range(len(searchWord)):
            while l <= r and (i >= len(products[l]) or products[l][i] != searchWord[i]):
                l += 1
            while l <= r and (i >= len(products[r]) or products[r][i] != searchWord[i]):
                r -= 1
                
            print(l, r)
                
            result.append([])
            for j in range(min(3, r - l + 1)):
                result[-1].append(products[l + j])

        return result
