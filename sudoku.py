import random
from collections import defaultdict
found = False
def check_invalid(matrix):
    # check for each row
    for row in range(len(matrix)):
        cur_row = set()
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                continue
            elif 1 <= matrix[row][col] <= 9:
                if matrix[row][col] in cur_row:
                    return False
                else:
                    cur_row.add(matrix[row][col])
            else:
                return False # invalid number
    # check each col
    for col in range(len(matrix[0])):
        cur_col = set()
        for row in range(len(matrix)):
            if matrix[row][col] == 0:
                continue
            elif 1 <= matrix[row][col] <= 9:
                if matrix[row][col] in cur_col:
                    return False
                else:
                    cur_col.add(matrix[row][col])
            else:
                return False # invalid number
    # check each 3*3 square
    for start_row in [0,3,6]:
        for start_col in [0,3,6]:
            cur_square = set()
            for row in range(start_row, start_row+3):
                for col in range(start_col, start_col + 3):
                    if matrix[row][col] == 0:
                        continue
                    elif 1 <= matrix[row][col] <= 9:
                        if matrix[row][col] not in cur_square:
                            cur_square.add(matrix[row][col])
                        else:
                            return False
                    else:
                        return False # invalid value
    return True

def resolve_sudoku(matrix, row_map, col_map, square_map, cur_row, cur_col):
    global found
    if found:
        return
    if cur_row == len(matrix):
        found = True
        for r in matrix:
            print r
    elif cur_col == len(matrix[0]):
        resolve_sudoku(matrix, row_map, col_map, square_map, cur_row+1, 0)
    elif matrix[cur_row][cur_col] != 0:
        resolve_sudoku(matrix, row_map, col_map, square_map, cur_row, cur_col+1)
    else:
        for val in range(1,10):
            square_x = cur_row / 3
            square_y = cur_col / 3
            if val in row_map[cur_row] or val in col_map[cur_col] or val in square_map[(square_x, square_y)]:
                continue
            else:
                row_map[cur_row].add(val)
                col_map[cur_col].add(val)
                square_map[(square_x, square_y)].add(val)
                matrix[cur_row][cur_col] = val
                resolve_sudoku(matrix, row_map, col_map, square_map, cur_row, cur_col+1)
                row_map[cur_row].remove(val)
                col_map[cur_col].remove(val)
                square_map[(square_x, square_y)].remove(val)
                matrix[cur_row][cur_col] = 0
                if found:
                    return
if __name__ == "__main__":
    matrix = []
    for row in range(9):
        cur_row = []
        for col in range(9):
            if random.random() < 0.1:
                cur_row.append(random.randint(1,9))
            else:
                cur_row.append(0)
        matrix.append(cur_row)
    for r in matrix:
        print r
    re = check_invalid(matrix)
    print re
    if re:
        # init for row map and col map
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                square_x = row / 3
                square_y = row / 3
                if matrix[row][col] != 0:
                    row_map[row].add(matrix[row][col])
                    col_map[col].add(matrix[row][col])
                    square_map[(row, col)].add(matrix[row][col])
        resolve_sudoku(matrix, row_map, col_map, square_map, 0, 0)
