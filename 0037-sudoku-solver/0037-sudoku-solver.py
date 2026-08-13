class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def solve():
            min_options = 10
            best_row = -1
            best_col = -1
            best_nums = []

            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        nums = []

                        for num in "123456789":
                            valid = True

                            for i in range(9):
                                if board[row][i] == num or board[i][col] == num:
                                    valid = False
                                    break

                            if valid:
                                r = (row // 3) * 3
                                c = (col // 3) * 3

                                for i in range(r, r + 3):
                                    for j in range(c, c + 3):
                                        if board[i][j] == num:
                                            valid = False
                                            break

                            if valid:
                                nums.append(num)

                        if len(nums) < min_options:
                            min_options = len(nums)
                            best_row = row
                            best_col = col
                            best_nums = nums

                        if min_options == 1:
                            break

                if min_options == 1:
                    break

            if best_row == -1:
                return True

            for num in best_nums:
                board[best_row][best_col] = num

                if solve():
                    return True

                board[best_row][best_col] = '.'

            return False

        solve()