# 1. ingest the grid into a list of lists
# 2. any tree that is visible is changed to a V, alternative is to maintain a parallel grid
# let's do it the easy way and keep tuples for each tree


def parse_forest(input_path):
    forest = []
    with open(input_path) as f:
        for line in f:
            forest.append([(int(height), 'N') for height in line.strip()])

    return forest


def is_tree_visible(grid):
    row = 0
    col = 0

    tallest_in_row = [{i: 0} for i in range(len(grid))]

    while col < len(grid[0]):
        tallest_in_col = 0
        row = 0

        while row < len(grid):
            tree_height = grid[row][col][0]

            if tree_height > tallest_in_col or col == 0:
                tallest_in_col = tree_height
                grid[row][col] = (tree_height, 'V')

            if tree_height > tallest_in_row[row] or row == 0:
                tallest_in_row[row] = tree_height
                grid[row][col] = (tree_height, 'V')

            row += 1

        col += 1

    row = len(grid) - 1
    col = len(grid[0]) - 1
    tallest_in_row = [{i: 0} for i in range(len(grid))]

    while col >= 0:
        tallest_in_col = 0
        row = len(grid) - 1

        while row >= 0:
            tree_height = grid[row][col][0]

            if tree_height > tallest_in_col or row == len(grid) - 1:
                tallest_in_col = tree_height
                grid[row][col] = (tree_height, 'V')

            if tree_height > tallest_in_row[row] or col == len(grid[0]) - 1:
                tallest_in_row[row] = tree_height
                grid[row][col] = (tree_height, 'V')

            row -= 1
        col -= 1

        return grid


g = parse_forest('input.txt')
print(is_tree_visible(g))
