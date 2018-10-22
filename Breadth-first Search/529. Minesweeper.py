class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        def counter(clickx):
            count_bomb = 0
            for i in range(max(0, clickx[0] - 1), min(len(board), clickx[0] + 2)):
                for j in range(max(0, clickx[1] - 1), min(clickx[1] + 2, len(board[0]))):
                    if board[i][j] == 'M':
                        count_bomb += 1
            return count_bomb

        count_bomb = counter(click)
        if count_bomb > 0:
            board[click[0]][click[1]] = str(count_bomb)
            return board

        def recurionhelper(clickx):
            countbomb = counter(clickx)
            if countbomb > 0:
                board[clickx[0]][clickx[1]] = str(countbomb)
                return
            else:
                for i in range(max(0, clickx[0] - 1), min(len(board), clickx[0] + 2)):
                    for j in range(max(0, clickx[1] - 1), min(clickx[1] + 2, len(board[0]))):
                        if board[i][j] == 'E':
                            print("pos: " + str(i) + ", " + str(j))
                            board[i][j] = 'B'
                            recurionhelper([i, j])

        recurionhelper(click)
        return board
