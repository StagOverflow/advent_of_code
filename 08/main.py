# 1. ingest the grid into a list of lists
# 2. any tree that is visible is changed to a V, alternative is to maintain a parallel grid
# let's do it the easy way and keep tuples for each tree


def parse_forest(input_path):
    forest = []
    with open(input_path) as f:
        for line in f:
            forest.append([(int(height), 'N') for height in line.strip()])

    return forest


def inspect_rows(grid, reversed_order=False):
    num_rows = len(grid)
    num_cols = len(grid[0])

    tallest_in_col = {}

    for i in range(num_cols):
        tallest_in_col[i] = 0

    row_range = range(0, num_rows)
    col_range = range(0, num_cols)

    if reversed_order:
        row_range = list(reversed(row_range))
        col_range = list(reversed(col_range))

    for row in row_range:
        tallest_in_row = 0
        for col in col_range:
            tree_height = grid[row][col][0]

            if tree_height == 4:
                print(44444)
            if tree_height > tallest_in_col[col] or col in (0, num_cols - 1):
                tallest_in_col[col] = tree_height
                grid[row][col] = (tree_height, 'V')

            if tree_height > tallest_in_row or row in (0, num_rows - 1):
                tallest_in_row = tree_height
                grid[row][col] = (tree_height, 'V')
    return grid


def get_tree_scenic_score(grid, col, row):
    top_limit = 1
    bottom_limit = len(grid) - 1
    right_limit = len(grid[0]) - 1
    left_limit = 1

    top_score = 1
    bottom_score = 1
    right_score = 1
    left_score = 1

    tree_height = grid[row][col][0]

    if col == 3 and row == 3:
        print("booom")

    if col in (left_limit, right_limit - 1) or row in (top_limit, bottom_limit - 1):
        return 0


    current_row = row - 1
    while current_row >= top_limit and tree_height > grid[current_row][col][0]:
        current_row -= 1
        top_score += 1

    current_row = row + 1
    while current_row < bottom_limit and tree_height > grid[current_row][col][0]:
        current_row += 1
        bottom_score += 1

    current_row = row
    current_col = col - 1
    while current_col >= left_limit and tree_height > grid[row][current_col][0]:
        current_col -= 1
        left_score += 1

    current_row = row
    current_col = col + 1
    while current_col < right_limit and tree_height > grid[current_row][current_col][0]:
        current_col += 1
        right_score += 1

    return left_score * top_score * right_score * bottom_score


def is_tree_visible(grid):
    checked_grid = inspect_rows(grid)
    reversed_checked_grid = inspect_rows(checked_grid, reversed_order=True)
    return reversed_checked_grid


def count_visible_trees(grid):
    count = 0
    for row in grid:
        for tree in row:
            count = count+1 if tree[1] == 'V' else count
    return count

def highest_scenic_score(grid):
    top_score = 0

    for row_i in range(len(grid)):
        for col_i in range(len(grid)):
            score = get_tree_scenic_score(grid, col_i, row_i)
            top_score = score if score > top_score else top_score
            print(f"{row_i},{col_i}:{grid[row_i][col_i]}|{score}")
    return top_score

def pretty_print(grid):
    for row in grid:
        print(row)


g = parse_forest('sample.txt')
print("from file: ")
pretty_print(g)
g = is_tree_visible(g)
print("visible trees: ")
pretty_print(g)
print(count_visible_trees(g))
print("highest scenic score")
print(highest_scenic_score(g))
