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

    if not reversed_order:
        rows = range(0, num)
        col = 0
    else:
        row = num_rows - 1
        col = num_cols - 1

    while row >= 0:
        tallest_in_row = 0
        col = num_cols - 1

        while col >= 0:
            tree_height = grid[row][col][0]

            if tree_height > tallest_in_col[col] or col in (0, num_cols - 1):
                tallest_in_col[col] = tree_height
                grid[row][col] = (tree_height, 'V')

            if tree_height > tallest_in_row or row in (0, num_rows - 1):
                tallest_in_row = tree_height
                grid[row][col] = (tree_height, 'V')

            col -= 1
        row -= 1

def is_tree_visible(grid):
    row = 0
    col = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    tallest_in_row = {}
    for i in range(num_rows):
        tallest_in_row[i] = 0

    while col < num_cols:
        tallest_in_col = 0
        row = 0

        while row < num_rows:
            tree_height = grid[row][col][0]

            if tree_height > tallest_in_col or col in (0, num_cols - 1):
                tallest_in_col = tree_height
                grid[row][col] = (tree_height, 'V')

            if tree_height > tallest_in_row[row] or row in (0, num_rows - 1):
                tallest_in_row[row] = tree_height
                grid[row][col] = (tree_height, 'V')

            row += 1
        col += 1

    row = num_rows - 1
    col = num_cols - 1
    tallest_in_col = {}

    for i in range(num_cols):
        tallest_in_col[i] = 0

    while row >= 0:
        tallest_in_row = 0
        col = num_cols - 1

        while col >= 0:
            tree_height = grid[row][col][0]

            if tree_height > tallest_in_col[col] or col in (0, num_cols - 1):
                tallest_in_col[col] = tree_height
                grid[row][col] = (tree_height, 'V')

            if tree_height > tallest_in_row or row in (0, num_rows - 1):
                tallest_in_row = tree_height
                grid[row][col] = (tree_height, 'V')

            col -= 1
        row -= 1

        return grid


def count_visible_trees(grid):
    count = 0
    for row in grid:
        for tree in row:
            count = count+1 if tree[1] == 'V' else count
    return count

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
