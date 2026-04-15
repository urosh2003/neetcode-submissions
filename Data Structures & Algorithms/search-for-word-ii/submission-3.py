class TrieNode:
    def __init__(self, char, i, j):
        self.char = char
        self.neighbors = {}
        self.i = i
        self.j = j
        self.visited = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        nodesCoords = {}
        nodesLetters = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                node = TrieNode(char, i, j)
                nodesCoords[(i, j)] = node
                if char not in nodesLetters:
                    nodesLetters[char] = []
                nodesLetters[char].append(node)
                if i > 0:
                    above = nodesCoords[(i-1, j)]
                    if char not in above.neighbors:
                        above.neighbors[char] = []
                    above.neighbors[char].append(node)

                    if above.char not in node.neighbors:
                        node.neighbors[above.char] = []
                    node.neighbors[above.char].append(above)

                    
                if j > 0:
                    above = nodesCoords[(i, j-1)]
                    if char not in above.neighbors:
                        above.neighbors[char] = []
                    above.neighbors[char].append(node)

                    if above.char not in node.neighbors:
                        node.neighbors[above.char] = []
                    node.neighbors[above.char].append(above)

        foundWords = []

        def find(root, word):
            if root.visited:
                return False
            if len(word) == 0:
                return True

            root.visited = True

            if word[0] in root.neighbors:
                for neighbor in root.neighbors[word[0]]:
                    found = find(neighbor, word[1:])
                    if found:
                        root.visited = False
                        return True

            root.visited = False
            return False

        for word in words:
            firstLetter = word[0]
            if firstLetter in nodesLetters:
                possible = True
                for letter in word:
                    if letter not in nodesLetters:
                        possible = False
                if possible:
                    for node in nodesLetters[firstLetter]:
                        found = find(node, word[1:])
                        if found:
                            foundWords.append(word)
                            break

        return foundWords