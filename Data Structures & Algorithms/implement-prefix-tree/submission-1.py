class TrieNode:
    def __init__(self, char, isWord = False):
        self.char = char
        self.children = [None] * 26
        self.isWord = isWord

    def addChild(self, char, isWord = False):
        index = ord(char) - ord('a')
        self.children[index] = TrieNode(char, isWord)


class PrefixTree:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        current = self.root
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.addChild(char)
            current = current.children[index]
            if i == len(word) - 1:
                current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            index = ord(char) - ord('a')
            if not current.children[index]:
                return False
            current = current.children[index]
        return True
        
        