class TrieNode:
    def __init__(self):
        self.nodeChars = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.nodeChars:
                node.nodeChars[char] = TrieNode()
            node = node.nodeChars[char]
        node.endOfWord = True
        

    def search(self, word: str) -> bool:
        def recursiveSearch(substring, node):
            if len(substring) == 0:
                return node.endOfWord
            
            char = substring[0]
            if char == '.':
                for childPtr in node.nodeChars.values():
                    if recursiveSearch(substring[1:], childPtr):
                        return True
            else:
                if char not in node.nodeChars:
                    return False
                return recursiveSearch(substring[1:], node.nodeChars[char])
        return recursiveSearch(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)