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
    top = row
    tree_height = grid[row][col][0]
    comparative_height = 0

    while comparative_height <= tree_height:



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

def pretty_print(grid):
    for row in grid:
        print(row)


g = parse_forest('input.txt')
print("from file: ")
pretty_print(g)
g = is_tree_visible(g)
print("visible trees: ")
pretty_print(g)
print(count_visible_trees(g))
