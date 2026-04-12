class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenX = [[False] * 10 for _ in range(9)]
        seenY = [[False] * 10 for _ in range(9)]
        seenGrid = [[False] * 10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                number = int(board[i][j])
                if seenX[i][number]:
                    print("SeenX")
                    print(i)
                    print(j)
                    print(number)
                    print(seenX)
                    return False
                else:
                    seenX[i][number] = True

                if seenY[j][number]:
                    print("SeenY")
                    print(i)
                    print(j)
                    print(number)
                    print(seenY)
                    return False
                else:
                    seenY[j][number] = True


                gridRow = (i // 3) * 3 + j //3
                 
                if seenGrid[gridRow][number]:
                    print("seenGrid")
                    print(i)
                    print(j)
                    print(number)
                    print(seenGrid)
                    return False
                else:
                    seenGrid[gridRow][number] = True



        return True
                