class Solution:
    def isValidSudoku(self, board):
        # 判断行中是否有重复数
        for row in board:
            temp_row = []
            for num in row:
                if num == '.':
                    continue
                if num not in temp_row:
                    temp_row.append(num)
                else:
                    return False
        # 判断列中是否有重复数
        i = 0
        while i <= 8:
            temp_col = []
            for row in board:
                if row[i] == '.':
                    continue
                elif row[i] not in temp_col:
                    temp_col.append(row[i])
                else:
                    return False
                continue
            i += 1
        x = board[0][1]

        # 判断方块中是否有重复数
        for i in range(0,9,3):
            for j in range(0, 9, 3):
                temp_block = []
                for row in range(i, i+3):
                    for col in range(j,j+3):
                        x = board[row][col]
                        if board[row][col] == '.':
                            continue
                        elif board[row][col] not in temp_block:
                            temp_block.append(board[row][col])
                        else:
                            return False
        return True             


if __name__ == "__main__":
    s = Solution()
    result = s.isValidSudoku(        [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]      ) 
    print(result)               

