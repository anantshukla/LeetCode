class TrieNode:
    def __init__(self):
        self.nodeChars = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.nodeChars:
                node.nodeChars[char] = TrieNode()
            node = node.nodeChars[char]
        node.endOfWord = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.nodeChars:
                return False
            node = node.nodeChars[char]
        return node.endOfWord
    
    # def search(self, word: str) -> bool:
    #     def recursiveSearch(substring, node):
    #         if len(substring) == 0:
    #             return node.endOfWord
            
    #         char = substring[0]
    #         if char not in node.nodeChars:
    #             return False
    #         return recursiveSearch(substring[1:], node.nodeChars[char])
    #     return recursiveSearch(word, self.root)


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.nodeChars:
                return False
            node = node.nodeChars[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)