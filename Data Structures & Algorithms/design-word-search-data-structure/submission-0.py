class TrieNode:
    def __init__(self, char, isWord = False):
        self.char = char
        self.children = [None] * 26
        self.isWord = isWord

    def addChild(self, char, isWord = False):
        index = ord(char) - ord('a')
        self.children[index] = TrieNode(char, isWord)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('')

    def addWord(self, word: str) -> None:
        current = self.root
        for i in range(len(word)):
            char = word[i]
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.addChild(char)
            current = current.children[index]
            if i == len(word) - 1:
                current.isWord = True

    def searchFromNode(self, root, word):
        if len(word) == 0:
            return root.isWord

        char = word[0]
        if char != '.':
            index = ord(char) - ord('a')
            if root.children[index]:
                return self.searchFromNode(root.children[index], word[1:])
            else:
                return False
        else:
            for child in root.children:
                if child:
                    found = self.searchFromNode(child, word[1:])
                    if found:
                        return True
            return False

    def search(self, word: str) -> bool:
        return self.searchFromNode(self.root, word)
